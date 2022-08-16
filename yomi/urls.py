from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.yomi, name='yomi'),
    path('kana', views.get_pinyin, name='get_pinyin')
]
