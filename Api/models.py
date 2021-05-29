from django.db import models


# Create your models here.


class Workout(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)
    muscle_worked = models.CharField(max_length=100)
    equipment = models.ManyToManyField(Equipment, blank=True)
    video_path = models.URLField(null=True, blank=True)
    image_path = models.URLField(null=True, blank=True)
    workout = models.ManyToManyField(Workout, blank=True)

    def __str__(self):
        return self.name
