from django.urls import path
from . import views


urlpatterns = [
    path('', views.liked_items),
]