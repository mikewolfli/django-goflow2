from django.contrib import admin

from goflow.runtime.models import ProcessInstance, WorkItem, Event, AuditEvent, WebhookEndpoint


class ProcessInstanceAdmin(admin.ModelAdmin):
    date_hierarchy = 'creationTime'
    list_display = ('title', 'process', 'process_version', 'user', 'creationTime', 'status', 'workitems_list')
    list_filter = ('process', 'status', 'user')
    fieldsets = (
              (None, {'fields':(
                                'title', 'process', 'user',
                                ('status', 'old_status'),
                                'condition',
                                ('object_id', 'content_type'))
                     }),
              )
admin.site.register(ProcessInstance, ProcessInstanceAdmin)


class WorkItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'user', 'instance', 'activity', 'status', 'events_list')
    list_filter = ('status', 'user', 'activity',)
    fieldsets = (
              (None, {'fields':(
                                ('instance', 'activity'),
                                'user',
                                'workitem_from',
                                ('status', 'blocked', 'priority'),
                                'push_roles', 'pull_roles',
                                ('created_at', 'activated_at', 'completed_at'),
                                ('sla_warned_at', 'sla_breached_at', 'last_escalation_at'))
                     }),
              )
admin.site.register(WorkItem, WorkItemAdmin)


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'name', 'workitem')
admin.site.register(Event, EventAdmin)


class AuditEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('created_at', 'action', 'actor', 'process', 'instance', 'workitem')
    list_filter = ('action', 'process')


admin.site.register(AuditEvent, AuditEventAdmin)


class WebhookEndpointAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'enabled')
    list_filter = ('enabled',)


admin.site.register(WebhookEndpoint, WebhookEndpointAdmin)
