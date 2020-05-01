from django import forms
from . import models


class TeamAnswerForm(forms.ModelForm):
    class Meta:
        model = models.TeamAnswer
        fields = [
            "answer",
            "team",
        ]


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            "name",
            "slug",
            "opentdb_session_key",
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = [
            "name",
            "quiz",
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            "answer",
            "correct",
            "question",
        ]


class RoundForm(forms.ModelForm):
    class Meta:
        model = models.Round
        fields = [
            "name",
            "position",
            "quiz",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "question",
            "position",
            "round",
        ]


class ActiveStateClass(forms.ModelForm):
    class Meta:
        model = models.ActiveState
        fields = [
            "quiz",
            "round",
            "question",
        ]
