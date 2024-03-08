from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api-v1'

router = DefaultRouter()
router.register('t', views.TeamViewSet, basename='team')
router.register('p', views.PlayerViewSet, basename='player')
router.register('b', views.BashgahViewSet, basename='bashgah')
router.register('tornoment', views.TornomentViewSet, basename='tornoment')
router.register('tc', views.TeamCompetitionViewSet, basename='team_competition')
router.register('gc', views.GroupCompetitionViewSet, basename='group_competition')

urlpatterns = [
    path('', include(router.urls)),
]