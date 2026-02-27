from django.urls import path
from goflow.graphics import views as goflow_graphics_views
urlpatterns = [
    path('processimage/<int:process_id>/pos_activity/', goflow_graphics_views.pos_activity),
]
