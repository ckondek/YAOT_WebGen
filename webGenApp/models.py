from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=128, unique = True)
    lastName = models.CharField(max_length=128, unique = True)
    twitter = models.CharField(max_length=128, unique = True)
    email_1 = models.EmailField(max_length=128, unique = True)
    email_2 = models.EmailField(max_length=128, unique = True)
    link_1 = models.URLField()
    link_2 = models.URLField()
