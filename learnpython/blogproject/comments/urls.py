from django.urls import path
from . import views

app_name = 'comments'  #指定命名空间
urlpatterns = [
    path('<int:article_pk>/', views.article_comment, name='article_comment'),
]