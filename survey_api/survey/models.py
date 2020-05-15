from django.db import models


# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name')
    datetime_start = models.DateTimeField(null=False,  verbose_name='Start datetime')
    datetime_finished = models.DateTimeField(null=False, verbose_name='Finish datetime')
    info = models.TextField(default='')


class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'free text'),
        ('select_one', 'select one'),
        ('select_many', 'select many'),
    ]
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=11, choices=QUESTION_TYPES)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, default=None)
    text = models.TextField(default='')
    user_id = models.IntegerField()
