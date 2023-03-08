# from django.conf.urls import url
from django.urls import path
from .views import createView, store, index
urlpatterns = [
    path('create/', createView),
    path('store/', store, name='store'),
    path('', index)
]