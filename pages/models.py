from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.SmallIntegerField()
    birthdate = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)

    def createperson(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.person


class Goals(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goalname = models.CharField(max_length=60)
    startdate = models.DateField()
    enddate = models.DateField()
    startingweight = models.SmallIntegerField()
    targetweight = models.SmallIntegerField()
    activitylevel = models.SmallIntegerField

    def __str__(self):
        return self.goalname
