from datetime import time
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField(null =True)
    preview_text = models.TextField(max_length=500)
    preview_image_url = models.URLField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author_name = models.CharField(max_length=200)
    comment_message = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk': self.post.pk})

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.comment_message
