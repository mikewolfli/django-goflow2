from django.urls import path, re_path, include
from . import forms
from . import views
from goflow.apptools.views import start_application,edit_model
from goflow.runtime.templatetags.work_lib import mywork
from goflow.runtime.views import activate, complete

urlpatterns = [
    # starting application
    path('start/', start_application, {'process_name':'Sample process',
                                        'form_class':forms.SampleModelForm,
                                        'template':'sample/start.html'}),
    # applications provided by goflow.apptools
    path('apptools/', include('goflow.apptools.urls')),
    # applications
    re_path(  r'^sample_edit/(?P<id>\d+)/$', edit_model, {'template':  'edit.html'}),
]

urlpatterns += [
    path('sample_myview/', views.myview),
]

urlpatterns += [
    path('mywork/', mywork, {'template':'sample/mywork.html'}),
    path('mywork/activate/<int:id>/', activate),
    path('mywork/complete/<int:id>/', complete)
]
