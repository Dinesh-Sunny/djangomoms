from django.db import models


class Post(models.Model):
    description = models.TextField()
    posted_at = models.DateTimeField()
    likes = models.IntegerField()
    summary = models.CharField(max_length=30, null=False)


class Comment(models.Model):
    description = models.TextField()
    posted_at = models.DateField()
    post = models.ForeignKey(Post)
