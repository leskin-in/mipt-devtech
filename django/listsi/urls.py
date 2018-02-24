from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.view_index),
    path('list/', include('list.urls')),
]
