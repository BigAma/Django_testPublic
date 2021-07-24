from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    auteur = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    question_label = models.CharField(max_length=100)
    question_text = models.TextField(max_length=600)
    question_pubdate = models.DateTimeField(auto_now_add=timezone.now(), blank=True)

    def __str__(self):
        return self.question_label

    def afficher_moins(self):
        return self.question_text[0:50]+" ..."

    def findbylabel(self):
        label = self.question_label
        return label


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
