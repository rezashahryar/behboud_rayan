from rest_framework.viewsets import ModelViewSet
from sport import models
from sport.models import GroupCompetition
from . import serializers


class TeamViewSet(ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class PlayerViewSet(ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class BashgahViewSet(ModelViewSet):
    queryset = models.Bashgah.objects.all()
    serializer_class = serializers.BashgahSerializer


class TornomentViewSet(ModelViewSet):
    queryset = models.Tornoment.objects.all()
    serializer_class = serializers.TornomentSerializer


class TeamCompetitionViewSet(ModelViewSet):
    queryset = models.TeamCompetition.objects.all()
    serializer_class = serializers.TeamCompetitionSerializer


class GroupCompetitionViewSet(ModelViewSet):
    queryset = models.GroupCompetition.objects.all()
    serializer_class = serializers.GroupCompetitionSerializer