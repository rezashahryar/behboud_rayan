from django.db import models
from django.conf import settings
# Create your models here.


class Bashgah(models.Model):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manager')
    coaches = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='coaches')
    name = models.CharField(max_length=255)
    location_of_bashgah = models.TextField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    bashgah = models.ForeignKey(Bashgah, on_delete=models.CASCADE, related_name='players', null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sport_field = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    weight = models.PositiveIntegerField(default=0)
    birth_date = models.DateField()
    code_melli = models.CharField(max_length=255)
    history_of_specific_disease = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Team(models.Model):
    bashgah = models.ForeignKey(Bashgah, on_delete=models.CASCADE, related_name='team', null=True)
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return self.name


class Tornoment(models.Model):
    STATUS_TORNOMENT_NOT_STARTED = 'not_started'
    STATUS_TORNOMENT = [
        (STATUS_TORNOMENT_NOT_STARTED, 'شروع نشده'),
        ('registering', 'قابل ثبت نام'),
        ('on_performing', 'در حال برگزاری'),
        ('end_of_tornoment', 'اتمام تورنومنت')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date_of_register = models.DateField()
    end_date_of_register = models.DateField()
    sport_field = models.CharField(max_length=55)
    # location
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tornoments')
    tornoment_status = models.CharField(max_length=20, choices=STATUS_TORNOMENT, default=STATUS_TORNOMENT_NOT_STARTED)

    def __str__(self):
        return self.title


class TeamCompetition(models.Model):
    COMPETITION_STATUS_NOT_STARTED = 'not_started'
    COMPETITION_STATUS = [
        (COMPETITION_STATUS_NOT_STARTED, 'شروع نشده'),
        ('on_performing', 'در حال برگزاری'),
        ('end', 'اتمام مسابقه'),
    ]
    first_participant = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='competition_as_first_team')
    second_participant = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='competition_as_second_team')
    date_of_competition = models.DateTimeField()
    location = models.TextField()
    competition_status = models.CharField(max_length=20, choices=COMPETITION_STATUS, default=COMPETITION_STATUS_NOT_STARTED)
    winer = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='winer')
    loser = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='loser')


class GroupCompetition(models.Model):
    COMPETITION_STATUS_NOT_STARTED = 'not_started'
    COMPETITION_STATUS = [
        (COMPETITION_STATUS_NOT_STARTED, 'شروع نشده'),
        ('on_performing', 'در حال برگزاری'),
        ('end', 'اتمام مسابقه'),
    ]
    players = models.ManyToManyField(Player)
    date_of_competition = models.DateTimeField()
    competition_status = models.CharField(max_length=20, choices=COMPETITION_STATUS, default=COMPETITION_STATUS_NOT_STARTED)
    location = models.TextField()


class ScoredInTheMatch(models.Model):
    ...