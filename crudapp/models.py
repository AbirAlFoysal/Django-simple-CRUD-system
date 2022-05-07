from turtle import update
import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateField(default=timezone.now)
    published = models.DateTimeField( auto_now_add=False)

    def get_absolute_url(self):
        return reverse('single', args=[self.slug])

    class Meta:
        ordering = ['-id']

    def __self__(self):
        return self.title
    