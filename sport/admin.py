from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.Tornoment)
admin.site.register(models.TeamCompetition)
admin.site.register(models.GroupCompetition)
admin.site.register(models.Bashgah)