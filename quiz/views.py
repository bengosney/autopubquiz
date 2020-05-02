from functools import lru_cache

import requests
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic

from . import models
from . import forms


class TeamAnswerListView(generic.ListView):
    model = models.TeamAnswer
    form_class = forms.TeamAnswerForm


class TeamAnswerCreateView(generic.CreateView):
    model = models.TeamAnswer
    form_class = forms.TeamAnswerForm


class TeamAnswerDetailView(generic.DetailView):
    model = models.TeamAnswer
    form_class = forms.TeamAnswerForm


class TeamAnswerUpdateView(generic.UpdateView):
    model = models.TeamAnswer
    form_class = forms.TeamAnswerForm
    pk_url_kwarg = "pk"


class QuizListView(generic.ListView):
    model = models.Quiz
    form_class = forms.QuizForm


class QuizCreateView(generic.CreateView):
    model = models.Quiz
    form_class = forms.QuizForm


class QuizDetailView(generic.DetailView):
    model = models.Quiz
    form_class = forms.QuizForm
    slug_url_kwarg = "slug"


class QuizUpdateView(generic.UpdateView):
    model = models.Quiz
    form_class = forms.QuizForm
    slug_url_kwarg = "slug"


class TeamListView(generic.ListView):
    model = models.Team
    form_class = forms.TeamForm


class TeamCreateView(generic.CreateView):
    model = models.Team
    form_class = forms.TeamForm


class TeamDetailView(generic.DetailView):
    model = models.Team
    form_class = forms.TeamForm


class TeamUpdateView(generic.UpdateView):
    model = models.Team
    form_class = forms.TeamForm
    pk_url_kwarg = "pk"


class AnswerListView(generic.ListView):
    model = models.Answer
    form_class = forms.AnswerForm


class AnswerCreateView(generic.CreateView):
    model = models.Answer
    form_class = forms.AnswerForm


class AnswerDetailView(generic.DetailView):
    model = models.Answer
    form_class = forms.AnswerForm


class AnswerUpdateView(generic.UpdateView):
    model = models.Answer
    form_class = forms.AnswerForm
    pk_url_kwarg = "pk"


class RoundListView(generic.ListView):
    model = models.Round
    form_class = forms.RoundForm


class RoundCreateView(generic.CreateView):
    model = models.Round
    form_class = forms.RoundForm


class RoundDetailView(generic.DetailView):
    model = models.Round
    form_class = forms.RoundForm


class RoundUpdateView(generic.UpdateView):
    model = models.Round
    form_class = forms.RoundForm
    pk_url_kwarg = "pk"


class QuestionListView(generic.ListView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionCreateView(generic.CreateView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionDetailView(generic.DetailView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionUpdateView(generic.UpdateView):
    model = models.Question
    form_class = forms.QuestionForm
    pk_url_kwarg = "pk"


class ActiveStateDetailView(generic.DetailView):
    model = models.ActiveState
    form_class = forms.ActiveStateClass


class QuizStartView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        quiz = models.Quiz.objects.get(slug=kwargs['slug'])
        running = models.ActiveState(quiz=quiz)
        running.save()

        return running.get_absolute_url()


class ActiveQuiz(generic.DetailView):
    model = models.ActiveState


class ActiveQuizControl(generic.DetailView):
    model = models.ActiveState
    template_name = 'quiz/activestate_control.html'

    def get(self, request, *args, **kwargs):
        active = self.get_object()

        if 'clear' in request.GET:
            active.round = None
            active.question = None

        if 'round' in request.GET:
            round_object = models.Round.objects.get(pk=request.GET['round'])
            active.round = round_object
            active.question = None

        if 'question' in request.GET:
            question_object = models.Question.objects.get(pk=request.GET['question'])
            active.question = question_object
            active.round = question_object.round
            active.save()

        active.save()

        return super().get(request, *args, **kwargs)
