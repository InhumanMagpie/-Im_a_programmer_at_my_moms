from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import ModelViewSet

from teamwork.models import User, Team
from teamwork.serializers import UserSerializer, TeamSerializer


class UsersViewSet(ModelViewSet):
    """Список всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'slug'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAdminOrManagerWithoutDeleteOrReadOnly]


class TeamViewSet(ModelViewSet):
    """Список команд"""
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
