import django
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.conf import settings
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from leave.forms import *
from goflow.workflow import views as goflow_workflow_views
from goflow.apptools import views as goflow_apptools_views
from goflow.workflow import notification as goflow_workflow_notification
from leavedemo.leave import views as leavedemo_leave_views


from leavedemo.leave import auto as leave_auto
from os.path import join, dirname
from django.views import static as django_views_static
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic as django_view_generic
from .api import api

from leavedemo.leave.forms import StartRequestForm, CheckRequestForm, RequesterForm, LeaveAttachmentFormSet

_dir = join(dirname(__file__))

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('api/', api.urls),
]

urlpatterns += i18n_patterns(
    re_path(r'^.*/accounts/login.*switch/(?P<username>.*)/(?P<password>.*)/$', goflow_workflow_views.debug_switch_user, {'redirect':'/leave/'}),
    re_path(r'^.*/switch/(?P<username>.*)/(?P<password>.*)/$', goflow_workflow_views.debug_switch_user),
    # user connection
    re_path(r'^.*/logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^.*/accounts/login/$', LoginView.as_view(template_name='goflow/login.html'),name='login'),
    
    # static
    re_path(r'^images/(?P<path>.*)$', django_views_static.serve, {'document_root': join(_dir, 'static/img'), 'show_indexes': True}),
    re_path(r'^files/(.*)$', django_views_static.serve, {'document_root': settings.MEDIA_ROOT}),
    
    # home redirection
    re_path(r'^.*/home/$', RedirectView.as_view(url='/leave/')),
 
    # home page
    path('leave/', TemplateView.as_view(template_name='leave.html')),
    
    # starting application
    
    #url(r'^leave/start/$', goflow_apptools_views.start_application, {'process_name':'leave',
    #                                                                       'form_class':StartRequestForm,
    #                                                                       'formset': LeaveAttachmentFormSet,
    #                                                                       'template':'start_leave.html'}),
    
    path('leave/start/', leavedemo_leave_views.start_leave_request,  {'process_name': 'leave',
                                                                       'form_class': StartRequestForm,
                                                                       'formset': LeaveAttachmentFormSet,
                                                                       'template': 'start_leave.html'}),
    
    # applications
    path('leave/checkstatus/<int:id>/', goflow_apptools_views.edit_model, {'form_class':CheckRequestForm,
                                                                                     'template':'checkstatus.html'}),
    path('leave/checkstatus_auto/', leavedemo_leave_views.checkstatus_auto, {'notif_user':True}),
    path('leave/refine/<int:id>/', goflow_apptools_views.edit_model, {'form_class':RequesterForm,
                                                                                'template':'refine.html'}),
    path('leave/approvalform/<int:id>/', goflow_apptools_views.edit_model, {'form_class':CheckRequestForm,
                                                                                      'template':'approval.html'}),
    path('leave/hrform/<int:id>/', goflow_apptools_views.view_application, {'template':'hrform.html'}),
    path('leave/hr_auto/', leave_auto.update_hr),
    path('leave/finalinfo/<int:id>/', goflow_apptools_views.view_application, {'template':'finalinfo.html'}),
    
     # administration
    path('leave/admin/apptools/', include('goflow.apptools.urls_admin')),
    path('leave/admin/workflow/', include('goflow.apptools.urls_admin')),
    path('leave/admin/graphics2/', include('goflow.graphics2.urls_admin')),
    path('leave/admin/', admin.site.urls ),
    #url(r'^admin/', admin.site.urls),

    # Goflow pages
    path('leave/', include('goflow.urls')),

    path('leave/send_mail/', goflow_workflow_notification.send_mail),


    
)
