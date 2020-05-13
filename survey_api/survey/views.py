from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Poll, Question
from .serializers import AdminPollSerializer, AdminQuestionSerializer, AdminPollCreateSerializer


# ADMIN
class AdminPollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = AdminPollSerializer
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
    serializer_class = AdminPollSerializer

