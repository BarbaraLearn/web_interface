
from django.urls import path

from . import views

urlpatterns = [
    #path("", views.home, name="home"),
    #path('upload/', views.upload_file, name='upload_file'),
    path('', views.upload_file, name='upload_file'),
    path('success/', views.download_file, name='download_file'), 
    # path('success/', views.upload_success, name='upload_success'),
    # path('download/', views.download_file, name='download_file'), 
]