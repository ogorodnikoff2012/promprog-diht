from django.db import models
from django.urls import reverse

class Question(models.Model):
    topic = models.CharField(max_length=80)
    text = models.CharField(max_length=2000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[' + self.topic + '] ' + self.text

    def answers(self):
        return self.answer_set.order_by('id')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.text
