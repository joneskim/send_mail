from django.urls.resolvers import URLPattern
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index)
]