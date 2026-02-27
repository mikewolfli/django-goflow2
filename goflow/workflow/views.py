#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest

from goflow.runtime.models import WorkItem
from goflow.workflow.models import *
from django.utils.translation import gettext_lazy as _, gettext
from django.contrib import messages


def index(request, template='workflow/index.html', extra_context={}):
    """workflow dashboard handler.
    
    template context contains following objects:
    - user
    - processes
    - roles
    
    other applications (ie runtime or apptools) should fill extra_context.
    """
    print('index request\n\n\n')
    me = request.user
    roles = Group.objects.all()
    processes = Process.objects.all()
    # optional package (ugly design)
    try:
        from goflow.apptools.models import DefaultAppModel
        obinstances = DefaultAppModel.objects.all()
    except Exception:
        obinstances = None
    
    context = {'processes':processes, 'roles':roles}
    context.update(extra_context)
    return render(request, template, context)


def debug_switch_user(request, username, password, redirect=None):
    """
    fast user switch for test purpose.
    
    parameters:
    
    username
        username
    password
        password
    redirect
        redirection url
    
    *FOR TEST ONLY*
    
    see template tag switch_users.
    """
    logout(request)
    # return HttpResponseRedirect(redirect)
    if not redirect:
        redirect = request.META['HTTP_REFERER']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(redirect)
        else:
            return HttpResponse(gettext('user is not active'))
    else:
        return HttpResponse(gettext('authentication failed'))


def userlist(request, template):
    '''
    not used
    '''
    return HttpResponse(gettext('user page.'))


def process_dot(request, id, template='goflow/process.dot'):
    """graphviz generator (**Work In Progress**).
    (**Work In Progress**)
    
    id process id
    template graphviz template
    
    context provides: process, roles, activities
    """
    process = Process.objects.get(id=int(id))
    context = {
               'process': process,
               'roles': ({'name':'role1', 'color':'red'},),
               'activities': Activity.objects.filter(process=process)
               }
    return render(request, template, context)


def cron(request=None):
    """
    (**Work In Progress**)
    TODO: move to instances ?
    """
    for t in Transition.objects.filter(condition__contains='workitem.timeout'):
        workitems = WorkItem.objects.filter(
            activity=t.input).exclude(status='complete')
        for wi in workitems:
            wi.forward(timeout_forwarding=True)
    
    if request:
        #request.user.message_set.create(message="cron has run.")
        messages.add_message(request, messages.INFO, "cron has run.")
        #if request.META.has_key('HTTP_REFERER'):
        if 'HTTP_REFERER' in request.META.keys():
            url = request.META['HTTP_REFERER']
        else:
            url = 'home/'
        return HttpResponseRedirect(url)


def workflow_designer(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Forbidden")
    process = Process.objects.get(id=process_id)
    return render(request, "goflow/workflow_designer.html", {"process": process})


def workflow_graph(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Forbidden")
    process = Process.objects.get(id=process_id)

    layout = WorkflowLayout.objects.filter(process=process).first()
    layout_map = layout.layout if layout else {}

    if request.method == "GET":
        activities = []
        for activity in Activity.objects.filter(process=process):
            position = layout_map.get(str(activity.id))
            activities.append(
                {
                    "id": activity.id,
                    "title": activity.title,
                    "kind": activity.kind,
                    "autostart": activity.autostart,
                    "autofinish": activity.autofinish,
                    "position": position,
                }
            )
        transitions = Transition.objects.filter(process=process).values(
            "id",
            "name",
            "input_id",
            "output_id",
            "condition",
        )
        payload = {
            "process": {
                "id": process.id,
                "title": process.title,
                "begin_id": process.begin_id,
                "end_id": process.end_id,
            },
            "activities": list(activities),
            "transitions": list(transitions),
        }
        return JsonResponse(payload)

    if request.method != "POST":
        return HttpResponseBadRequest("Unsupported method")

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    activities = data.get("activities", [])
    transitions = data.get("transitions", [])
    positions = data.get("positions", {})
    deleted_activity_ids = set(data.get("deleted_activity_ids", []))
    deleted_transition_ids = set(data.get("deleted_transition_ids", []))
    begin_id = data.get("begin_id")
    end_id = data.get("end_id")

    for activity_id in deleted_activity_ids:
        Activity.objects.filter(process=process, id=activity_id).delete()
        layout_map.pop(str(activity_id), None)

    for transition_id in deleted_transition_ids:
        Transition.objects.filter(process=process, id=transition_id).delete()

    activity_map = {}
    for item in activities:
        item_id = item.get("id")
        defaults = {
            "title": item.get("title", "Activity"),
            "kind": item.get("kind", "standard"),
            "autostart": bool(item.get("autostart", False)),
            "autofinish": bool(item.get("autofinish", True)),
        }
        if item_id:
            activity = Activity.objects.get(id=item_id, process=process)
            for field, value in defaults.items():
                setattr(activity, field, value)
            activity.save()
        else:
            activity = Activity.objects.create(process=process, **defaults)
        activity_map[item.get("client_id") or activity.id] = activity.id

        position = item.get("position")
        if position:
            layout_map[str(activity.id)] = position

    for item in transitions:
        item_id = item.get("id")
        input_id = item.get("input_id")
        output_id = item.get("output_id")
        if input_id in activity_map:
            input_id = activity_map[input_id]
        if output_id in activity_map:
            output_id = activity_map[output_id]
        if not input_id or not output_id:
            continue
        defaults = {
            "name": item.get("name") or "",
            "condition": item.get("condition") or "",
        }
        if item_id:
            transition = Transition.objects.get(id=item_id, process=process)
            transition.input_id = input_id
            transition.output_id = output_id
            transition.name = defaults["name"]
            transition.condition = defaults["condition"]
            transition.save()
        else:
            Transition.objects.create(
                process=process,
                input_id=input_id,
                output_id=output_id,
                name=defaults["name"],
                condition=defaults["condition"],
            )

    if begin_id in activity_map:
        begin_id = activity_map[begin_id]
    if end_id in activity_map:
        end_id = activity_map[end_id]

    if begin_id:
        process.begin_id = begin_id
    if end_id:
        process.end_id = end_id
    process.save()

    if positions:
        for key, value in positions.items():
            layout_map[str(key)] = value

    if layout:
        layout.layout = layout_map
        layout.save()
    else:
        WorkflowLayout.objects.create(process=process, layout=layout_map)

    return JsonResponse({"status": "ok"})

