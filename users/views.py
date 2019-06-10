from rest_framework.viewsets import ModelViewSet

from .models import Category, Role, User
from .serializers import CategorySerializer, RoleSerializer, UserSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class RoleViewSet(ModelViewSet):

    serializer_class = RoleSerializer
    queryset = Role.objects.all()

"""
    def get_queryset(self):
        g = Group.objects.filter(name='worker: Read')[0]
        user = User.objects.filter(email=self.request.user.email)[0]
        print('g {}'.format(g))
        if g in user.groups.all():
            return Event.objects.all()
        try:
            return Event.objects.filter(created_by=self.request.user)
            # return get_objects_for_user(user=self.request.user, with_superuser=False, perms=['events.view_event'], klass=Event)
        except Exception as e:
            print(e)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        g = Group.objects.filter(name='worker: Delete')[0]
        user = User.objects.filter(email=self.request.user.email)[0]
        if g in user.groups.all():
            return super().destroy(request)
        else:
            raise PermissionDenied

    def update(self, request, pk=None, *args, **kwargs):
        print('self:{}', self)
        print(Event.objects.filter(id=pk))
        result = 'worker: Update' in get_perms(request.user, Event.objects.filter(id=pk)[0])
        print(result)
"""