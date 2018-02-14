from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #adding the thumbnails as well
    thumb = models.ImageField(default='default.png', blank=True)
    #adding the author as well from djangogirls too
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    #common in both
    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def snippet(self):
        return self.body[0:50] + "..."