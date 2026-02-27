from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.static import serve
from .api import api

from goflow.workflow import views as goflow_workflow_views
from goflow.apptools import views as goflow_apptools_views
from goflow.workflow import notification as goflow_workflow_notification
from .sampleapp.views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('api/', api.urls),
]

urlpatterns += i18n_patterns(
    # django-flags for internationalization
    #url(r'^lang/', include('sampleproject.flags.urls')),
    # FOR DEBUG AND TEST ONLY
    re_path(r'^.*switch/(?P<username>.*)/(?P<password>.*)/$', goflow_workflow_views.debug_switch_user),
    # home page
    path('', home),
    # home redirection
    re_path(r'^.*home/$', RedirectView.as_view(url= '/')),
    # login/logout
    re_path(r'^.*/logout/$', LogoutView.as_view(), name='logout'), 
    path('accounts/login/', LoginView.as_view(template_name='goflow/login.html'), name='login'),

    # Example:
    path('sampleapp/', include('sampleproject.sampleapp.urls')),

    # Uncomment the next line to enable admin documentation:
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    
    # FOR TEST - insert before admin/(.*)
    path('admin/workflow/', include('goflow.apptools.urls_admin')),
    # special
    path('admin/apptools/', include('goflow.apptools.urls_admin')),
    
    # Uncomment the next line for to enable the admin:
    path('admin/', admin.site.urls),
    # workflow pages
    path('workflow/', include('goflow.urls')),
    # static files
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
)
