from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.view_main),
    path('notes/', include('notes.urls')),
]
