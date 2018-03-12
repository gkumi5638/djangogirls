from django.db import models

# Create your models here.
from django.utils import TIME_ZONE

class Post(models.Model)
    author = models.ForeighnKey('auth.User')
    title = models.Charfield(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
    default=timezone.now)
    published_date = models.DateTimeField(
    blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
