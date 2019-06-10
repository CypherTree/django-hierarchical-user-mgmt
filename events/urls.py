# from .views import LocationViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CreateEventView, ListEventView, RUDEventView



urlpatterns = [
    (path('event/create', CreateEventView.as_view({'post':'create'}))),
    (path('event/list', ListEventView.as_view({'get': 'list'}))),
    (path('event/rud/<pk>', RUDEventView.as_view({'get': 'retrieve', 'put': 'update', 'delete':'destroy'}))),
]