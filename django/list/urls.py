from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_note_queue, name='list'),
]
