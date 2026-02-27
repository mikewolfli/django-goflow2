from django.contrib import admin

from django.contrib.auth import get_user_model
from goflow.workflow.admin import GoFlowUserAdmin, UserProfileInline
from leavedemo.leave.models import *

User = get_user_model()


class LeaveRequestAdmin(admin.ModelAdmin):
    fieldsets = (
              (None, {'fields':('day_start', 'day_end', 'type', 'requester', 'reason', 'reason_denial')}),
              )
    list_display = ('type', 'date', 'day_start', 'day_end', 'requester')
    list_filter = ('type', 'requester')
admin.site.register(LeaveRequest, LeaveRequestAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'days')
admin.site.register(Account, AccountAdmin)


class ManagerInline(admin.TabularInline):
    model = Manager
    max_num = 1

admin.site.unregister(User)

class LeaveUserAdmin(GoFlowUserAdmin):
    inlines = [UserProfileInline, ManagerInline]
admin.site.register(User, LeaveUserAdmin)
