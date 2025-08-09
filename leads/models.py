from django.db import models

# Create your models here.
class Lead(models.Model):

    SOURCE_CHOICE = (
        ('YouTuBe', 'YouTuBe'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICE, max_length=100)
    profile_picture = models.ImageField(blank=True , null=True)