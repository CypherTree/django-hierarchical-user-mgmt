from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import  ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework_rules.mixins import PermissionRequiredMixin


from .models import Event
from .serializers import EventSerializer

# Create your views here.

class CreateEventView(PermissionRequiredMixin, CreateModelMixin, GenericViewSet):

    object_permission_required = 'event_app.create_event'
    permission_required = 'event_app.create_event'

    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ListEventView(PermissionRequiredMixin, ListModelMixin, GenericViewSet):
    permission_required = 'event_app.list_events'

    serializer_class = EventSerializer
    queryset = Event.objects.all()


class RUDEventView(PermissionRequiredMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):

    permission_required = 'event_app.delete_event'
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @detail_route(methods=['get'], permission_required='event_app.list_events')
    def retrieve(self, request, pk, **kwargs):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(data=serializer.data)

    def put(self, request, pk, **kwargs):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
