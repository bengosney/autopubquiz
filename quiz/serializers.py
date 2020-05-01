from rest_framework import serializers

from . import models


class TeamAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TeamAnswer
        fields = [
            "last_updated",
            "created",
        ]

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = [
            "last_updated",
            "name",
            "slug",
            "created",
            "opentb_session_key",
        ]

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Team
        fields = [
            "created",
            "last_updated",
            "name",
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = [
            "answer",
            "correct",
            "last_updated",
            "created",
        ]

class RoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Round
        fields = [
            "last_updated",
            "created",
            "name",
            "position",
        ]

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = [
            "question",
            "last_updated",
            "position",
            "created",
        ]
