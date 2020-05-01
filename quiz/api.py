from rest_framework import viewsets, permissions

from . import serializers
from . import models


class TeamAnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for the TeamAnswer class"""

    queryset = models.TeamAnswer.objects.all()
    serializer_class = serializers.TeamAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuizViewSet(viewsets.ModelViewSet):
    """ViewSet for the Quiz class"""

    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for the Team class"""

    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Answer class"""

    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoundViewSet(viewsets.ModelViewSet):
    """ViewSet for the Round class"""

    queryset = models.Round.objects.all()
    serializer_class = serializers.RoundSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Question class"""

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
