from django.urls import path
from . import views


urlpatterns = [
    path('get', views.get_note_list),
    path('add', views.add_note),
    path('delete', views.delete_note)
]
