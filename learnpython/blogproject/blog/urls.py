from django.urls import path
from . import views

app_name = 'blog'  #指定命名空间
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:year>/<int:month>/', views.archive, name='archive'),
    path('category/<int:pk>/', views.category, name='category'),
    #path('<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
]
