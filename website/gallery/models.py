from django.db import models

class Biodata(models.Model):
    name = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    location = models.CharField(max_length=550)
    email = models.CharField(max_length=250)
    linkedin_url = models.CharField(max_length=250)
    twitter = models.CharField(max_length=300)

    

    
