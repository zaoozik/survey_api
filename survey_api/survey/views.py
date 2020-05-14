from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Poll, Question, Answer
from .serializers import PollSerializer, AdminQuestionSerializer, AdminPollCreateSerializer, UserAnswerSerializer


# ADMIN
class AdminPollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request):
        serializer = AdminPollCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AdminQuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = AdminQuestionSerializer
    permission_classes = [permissions.IsAdminUser]


# USER
class UserPollsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


@api_view(['GET'])
def get_poll_questions(request, poll_id):
    queryset = Question.objects.get(poll_id__exact=poll_id)
    serializer = AdminQuestionSerializer(queryset)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def handle_poll_question(request, poll_id, question_id):
    if request.method == 'GET':
        queryset = Question.objects.get(poll_id__exact=poll_id, pk=question_id)
        serializer = AdminQuestionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        data['question'] = question_id
        serializer = UserAnswerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_user_answers(request, user_id):
    answers = Answer.objects.get(user_id__exact=user_id)
    polls = Answer.objects.get(user_id__exact=user_id).join(Question.objects.)
    serializer = AdminQuestionSerializer(answers)
    return Response(serializer.data, status=status.HTTP_200_OK)
