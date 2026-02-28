import django.db.models
from django.apps import apps
from django.contrib.auth import get_user_model
from goflow.workflow.models import *
DEBUG = True
User = get_user_model()

def log(section, variable):
    if DEBUG:
        print('adding [%s] %s' % (section, variable))
    else:
        pass

# ------------------------------------------------------------------------------------
# a class based Process Builder for GoFlow
# ------------------------------------------------------------------------------------
class ProcessBuilder(object):
    def __init__(self, title='', description='', enabled=True, priority=0,
            start_activity='begin', end_activity='end'):
        self.process = self.create_process(title=title, description=description,
                                           enabled=enabled, priority=priority)
        self.process_role = self.create_process_role()
        self.start_activity = start_activity
        self.end_activity = end_activity
        self.users = {}
        self.roles = {}
        self.applications = {}
        self.activities = {}
        self.transitions = {}

    def add_application(self, url='', suffix='w'):
        app = Application(url=url, suffix=suffix)
        log('application', app)
        app.save()
        return app

    def add_applications(self, applications):
        self.applications = applications

    def add_pushapp(self, url=None):
        if url:
            pushapp, new = PushApplication.objects.get_or_create(url=url)
            if new:
                pushapp.save()
            return pushapp
        else:
            return

    def add_activity(self, title='', description='', kind='standard',
            push_application=None, pushapp_param='', application='',
            app_param='', autostart=False, autofinish=True,
            join_mode='and', split_mode='xor', roles=[], node_type='standard',
            form_template=None, form_class=None):
        '''
        creates a single activity instance
        '''
        activity = Activity(title=title, description=description, kind=kind,
            process=self.process, push_application=push_application,
            pushapp_param=pushapp_param, application=application,
            app_param=repr(app_param), autostart=autostart, autofinish=autofinish,
            join_mode=join_mode, split_mode=split_mode,
            node_type=node_type, form_template=form_template, form_class=form_class,
        )
        log('activity', activity)
        activity.save()
        for role in roles:
            activity.roles.add(self.roles[role])
        activity.save()
        self.activities[title] = activity
        return activity

    def add_activities(self, activities):
        _activities = []
        for item in activities:
            if len(item) == 9:
                title, kind, pushapp, app, autostart, autofinish, join, split, roles = item
                node_type = 'standard'
                form_template = None
                form_class = None
            else:
                title, kind, pushapp, app, autostart, autofinish, join, split, roles, node_type, form_template, form_class = item
            _activities.append(self.add_activity(
                title=title, kind=kind, push_application=self.add_pushapp(pushapp),
                application=self.add_application(url=self.applications[app]['url']),
                app_param=self.applications[app]['parameters'],
                autostart=autostart, autofinish=autofinish,
                join_mode=join, split_mode=split, roles=roles,
                node_type=node_type, form_template=form_template, form_class=form_class,
            ))
        return _activities

    def add_transition(self, input_output=(None, None), name='', condition='', pre_hook=None, post_hook=None):
        input=self.activities[input_output[0]]
        output=self.activities[input_output[1]]
        t = Transition(name=name, process=self.process, input=input,
            output=output, condition=condition, pre_hook=pre_hook, post_hook=post_hook)
        log('transition', t)
        t.save()
        self.transitions[name] = t
        return t

    def add_transitions(self, transitions):
        ts = []
        for item in transitions:
            if len(item) == 3:
                input_output, name, condition = item
                pre_hook, post_hook = None, None
            else:
                input_output, name, condition, pre_hook, post_hook = item
            ts.append(self.add_transition(input_output, name, condition, pre_hook, post_hook))
        return ts

    def create_process(self, title='', begin=None, end=None,
            description='', enabled=True, priority=0):
        process = Process(title=title, description=description,
            enabled=enabled, priority=priority)
        log('process', process)
        process.begin = begin
        process.end = end
        process.save()
        return process

    def create_process_role(self):
        process_role = Group.objects.create(name=self.process.title)
        log('role|group', process_role)
        process_ctype = ContentType.objects.get_for_model(Process)
        can_instantiate_permission = Permission.objects.get(content_type=process_ctype,
            codename='can_instantiate')
        process_role.permissions.add(can_instantiate_permission)
        log('permission', can_instantiate_permission)
        return process_role

    def add_user(self, name, email, password,
            is_staff=True, is_active=True, is_superuser=False, roles=[]):
        '''
        This is the least generic, but that is deliberate to fully
        test everything.
        '''
        user = User.objects.create_user(name, email, password)
        log('user', user)
        if is_staff: user.is_staff=True
        if is_active: user.is_active=True
        #TODO: this is just for testing and will/should be removed
        if name == 'admin': user.is_superuser = True
        if roles:
            for rolename in roles:
                role = Group.objects.get(name=rolename)
                user.groups.add(role)
                log('%s.role' % user.username, role)
        user.save()
        self.users[name] = user
        return user

    def add_users(self, users=[]):
        _users = []
        for name, email, password, roles in users:
            _users.append(self.add_user(name=name, email=email, password=password,
                roles=roles))
        return _users

    def add_role(self, name, permissions):
        '''
        e.g. add_role('accountant', [('finance','BusinessPlan', 'can_review')])
        '''
        role, flag = Group.objects.get_or_create(name=name)
        log('role', role)
        for app_label, model_class_name, codename in permissions:
            model_class = apps.get_model(app_label, model_class_name)
            content_type = ContentType.objects.get_for_model(model_class)
            permission = Permission.objects.get(content_type=content_type,
                codename=codename)
            role.permissions.add(permission)
            log('%s.permission' % role.name, permission)
        role.save()
        self.roles[name] = role
        return role

    def add_roles(self, roles=[]):
        _roles = []
        for name, permissions in roles:
            _roles.append(self.add_role(name, permissions))
        return _roles

    def setup_all(self):
        self.process.begin = self.activities[self.start_activity]
        self.process.end = self.activities[self.end_activity]
        self.process.save()

    def as_graph(self, to=None):
        from pygraphviz import AGraph
        g = AGraph(directed=True)

        for a in list(self.activities.values()):
            g.add_node(a.title, label=a.title)

        for t in list(self.transitions.values()):
            g.add_edge(t.input.title, t.output.title, label=t.name)

        if to:
            g.write(to)
        else:
            return str(g)

