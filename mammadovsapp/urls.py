from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('kateqoriya/<str:article_category>/<slug:article_slug>', views.article, name='article'),
    path('kateqoriya/<str:category_name>', views.list_of_post),
    path('elaqe/', views.contact, name='contact'),
    path('haqqimda/', views.about, name='about'),
]

