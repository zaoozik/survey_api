from .models import Question, Answer, Choice, Poll
from rest_framework import serializers


class AdminQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ['datetime_start']


class AdminPollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class UserPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text']

