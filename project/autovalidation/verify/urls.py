from django.urls import path
from . import  views

app_name = 'verify'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('verify/', views.verify, name='verify'),
    path('export/', views.export, name='export'),
    path('migrate/', views.migrate, name='migrate'),
]