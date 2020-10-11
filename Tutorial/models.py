from django.db import models

# Create your models here.
class Question(models.Model):
    ques = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.ques

class Reply(models.Model):
    reply_ans = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.reply_ans

