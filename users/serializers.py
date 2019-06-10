
from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import User, Category, Role


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'role', 'category'  )

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

class RoleSerializer(ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name')
