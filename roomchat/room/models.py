from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    maps_link = models.CharField(max_length=500, default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d91160.57954789397!2d26.012237353149633!3d44.437918701576166!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40b1f93abf3cad4f%3A0xac0632e37c9ca628!2sBucure%C8%99ti!5e0!3m2!1sro!2sro!4v1704033346511!5m2!1sro!2sro')
    getformio_link = models.CharField(max_length=500, default='https://getform.io/f/1d572e0e-f9aa-4867-b9a5-aa272944480f')
    Opositive = models.IntegerField(blank=True, null=True)
    Onegative = models.IntegerField(blank=True, null=True)
    Apositive = models.IntegerField(blank=True, null=True)
    Anegative = models.IntegerField(blank=True, null=True)
    Bpositive = models.IntegerField(blank=True, null=True)
    Bnegative = models.IntegerField(blank=True, null=True)
    ABpositive = models.IntegerField(blank=True, null=True)
    ABnegative = models.IntegerField(blank=True, null=True)
