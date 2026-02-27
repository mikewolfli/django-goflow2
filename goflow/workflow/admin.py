from django.contrib import admin
from django import forms
from django.db.models import *

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from goflow.workflow.models import Transition, Process, Application, PushApplication, Activity, UserProfile

User = get_user_model()


class TransitionInline(admin.StackedInline):
    model = Transition
    fieldsets = (
              (None, {'fields':(('input', 'output'), 'condition', 'precondition')}),
              )


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled', 'summary', 'priority')
    inlines = [
                   TransitionInline,
               ]


admin.site.register(Process, ProcessAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('url', 'documentation', 'test')


admin.site.register(Application, ApplicationAdmin)


class PushApplicationAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('url', 'documentation', 'test')


admin.site.register(PushApplication, PushApplicationAdmin)


class ActivityAdminForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActivityAdminForm, self).__init__(*args, **kwargs)
        self.fields['app_param'].help_text = (
            'Use JSON/object mapping, e.g. {"template": "start_leave.html", "ok_values": ["APPROVED", "REJECTED"]}. '
            'Python eval expressions are not supported.'
        )
        self.fields['pushapp_param'].help_text = (
            'Use JSON/object mapping, e.g. {"username": "john"}. Python eval expressions are not supported.'
        )
        self.fields['app_param'].widget.attrs['placeholder'] = '{"template":"start_leave.html"}'
        self.fields['pushapp_param'].widget.attrs['placeholder'] = '{"username":"john"}'


class TransitionAdminForm(forms.ModelForm):
    class Meta:
        model = Transition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TransitionAdminForm, self).__init__(*args, **kwargs)
        self.fields['condition'].help_text = (
            'Safe condition DSL examples: eq:APPROVED, ne:REJECTED, in:APPROVED,OK, timeout:3d, '
            'or safe expression like instance.condition == "APPROVED".'
        )
        self.fields['condition'].widget.attrs['placeholder'] = 'eq:APPROVED | timeout:3d'


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityAdminForm
    save_as = True
    list_display = ('title', 'description', 'kind', 'application',
                    'join_mode', 'split_mode', 'autostart', 'autofinish', 'process')
    list_filter = ('process', 'kind')
    fieldsets = (
              (None, {'fields':(('kind', 'subflow'), ('title', 'process'), 'description')}),
              ('Push application', {'fields':(('push_application', 'pushapp_param'),)}),
              ('Application', {'fields':(('application', 'app_param'),)}),
              ('I/O modes', {'fields':(('join_mode', 'split_mode'),)}),
              ('Execution modes', {'fields':(('autostart', 'autofinish'),)}),
              ('Permission', {'fields':('roles',)}),
              )


admin.site.register(Activity, ActivityAdmin)


class TransitionAdmin(admin.ModelAdmin):
    form = TransitionAdminForm
    save_as = True
    list_display = ('__str__', 'input', 'output', 'condition', 'description', 'process')
    list_filter = ('process',)
    fieldsets = (
              (None, {'fields':(
                                ('name', 'description'),
                                'process',
                                ('input', 'output'),
                                'condition', 'precondition'
                                )
                     }),
              )


admin.site.register(Transition, TransitionAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'web_host', 'notified', 'last_notif', 'nb_wi_notif', 'notif_delay')
    list_filter = ('web_host', 'notified')


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1


class GoFlowUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.register(User, GoFlowUserAdmin)
