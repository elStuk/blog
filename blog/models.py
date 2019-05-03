from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, related_name='post_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
