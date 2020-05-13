from .models import Question, Answer, Choice, Poll
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ['datetime_start']


class PollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
