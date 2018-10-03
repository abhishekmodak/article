from django.db import models

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    vote = models.IntegerField(default=0)
    added_at   = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status  = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def upvote(self):
        self.vote += 1
        self.save()