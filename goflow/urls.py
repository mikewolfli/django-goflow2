from django.urls import path,re_path, include #django 2.*

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

from goflow.apptools.forms import DefaultAppStartForm
from goflow.apptools.views import start_application, default_app
from goflow.runtime.views import *
from goflow.workflow.views import process_dot, index, cron, workflow_designer, workflow_graph

urlpatterns = [
    re_path(r'^.*/logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^.*/accounts/login/$', LoginView.as_view(template_name='goflow/login.html')),
    path('apptools/', include('goflow.apptools.urls')),
    path('graph/', include('goflow.graphics.urls')),
]

urlpatterns += [
    path('', index),
    path('process/dot/<int:id>/',process_dot),
    path('cron/', cron),
    path('designer/<int:process_id>/', workflow_designer),
    path('designer/<int:process_id>/graph/', workflow_graph),
    ]

urlpatterns += [
    path('default_app/<int:id>/', default_app),
    re_path(r'^start/(?P<app_label>.*)/(?P<model_name>.*)/$', start_application),
    re_path(r'^start_proto/(?P<process_name>.*)/$', start_application,
        {'form_class':DefaultAppStartForm,
         'redirect':'../../',
         'template':'goflow/start_proto.html'}),
]

urlpatterns += [
    path('otherswork/',                 otherswork),
    path('otherswork/instancehistory/', instancehistory),
    path('myrequests/',                 myrequests),
    path('myrequests/instancehistory/', instancehistory),
    path('mywork/',                     mywork),
    path('mywork/activate/<int:id>/', activate),
    path('mywork/complete/<int:id>/', complete),
]

