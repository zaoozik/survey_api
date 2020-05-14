import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Poll, Question, Answer, Choice
from .serializers import PollSerializer, AdminQuestionSerializer, AdminPollCreateSerializer, UserAnswerSerializer, \
    UserQuestionSerializer, UserChoiceSerializer


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
    queryset = Question.objects.filter(poll_id__exact=poll_id)
    response = []
    for question in queryset:
        temp = dict(UserQuestionSerializer(question).data)
        if question.type != "text":
            choices = Choice.objects.filter(question_id__exact=question.pk)
            temp["choices"] = UserChoiceSerializer(choices, many=True).data
        response.append(temp)

    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


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
    answers = Answer.objects.filter(user_id__exact=user_id).select_related('question')
    polls = []
    questions = []
    for a in answers:
        polls.append(a.question.poll)
        questions.append(a.question)
    polls = set(polls)
    response = []
    for poll in polls:
        temp = {
            "id": poll.pk,
            "name": poll.name,
            "questions": []
        }
        questions = Question.objects.filter(poll_id__exact=poll.pk)
        for question in questions:
            answer = answers.get(question_id__exact=question.id)
            temp['questions'].append(
                {
                    "id": question.id,
                    "text": question.text,
                    "answer": answer.text
                }
            )
        response.append(temp)

    return JsonResponse(response, safe=False, status=status.HTTP_200_OK)

