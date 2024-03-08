from rest_framework import serializers
from ... import models


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['bashgah', 'name', 'players']


class PlayerSerializer(serializers.ModelSerializer):
    bashgah = serializers.StringRelatedField()

    class Meta:
        model = models.Player
        fields = ['bashgah', 'first_name', 'last_name', 'sport_field', 'mobile_number', 'weight', 'birth_date'
            , 'code_melli', 'history_of_specific_disease', 'description']


class BashgahSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bashgah
        fields = ['name', 'manager', 'coaches', 'location_of_bashgah', 'phone_number', 'description']


class TornomentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tornoment
        fields = ['title', 'description', 'start_date_of_register', 'end_date_of_register', 'sport_field', 'owner', 'tornoment_status']


class TeamCompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TeamCompetition
        fields = ['first_participant', 'second_participant', 'date_of_competition', 'location', 'competition_status', 'winer', 'loser']


class GroupCompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GroupCompetition
        fields = ['players', 'date_of_competition', 'competition_status', 'location']