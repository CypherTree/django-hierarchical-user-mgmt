from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ('name', 'slug', 'location', 'created_by' )
