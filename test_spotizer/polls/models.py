from django.db import models


class Style(models.Model):
    style = models.CharField()


class Artiste(models.Model):
    nom = models.CharField(max_lenght=200)
    style = models.ForeignKey(Style)
    image = models.ImageField()


class Album(models.Model):
    artiste = models.ForeignKey(Artiste)
    nom = models.CharField(max_lenght=200)
    date = models.DateField()
    image = models.ImageField()


class Morceau(models.Model):
    album = models.ForeignKey(Album)
    nom = models.CharField()
    file = models.FileField()