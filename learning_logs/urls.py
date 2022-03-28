"""learning_logs の URL パターンの定義"""

from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
]