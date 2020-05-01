from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("TeamAnswer", api.TeamAnswerViewSet)
router.register("Quiz", api.QuizViewSet)
router.register("Team", api.TeamViewSet)
router.register("Answer", api.AnswerViewSet)
router.register("Round", api.RoundViewSet)
router.register("Question", api.QuestionViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    # path("teamanswer/", views.TeamAnswerListView.as_view(), name="quiz_teamanswer_list"),
    # path("teamanswer/create/", views.TeamAnswerCreateView.as_view(), name="quiz_teamanswer_create"),
    # path("teamanswer/detail/<int:pk>/", views.TeamAnswerDetailView.as_view(), name="quiz_teamanswer_detail"),
    # path("teamanswer/update/<int:pk>/", views.TeamAnswerUpdateView.as_view(), name="quiz_teamanswer_update"),
    path("", views.QuizListView.as_view(), name="quiz_quiz_list"),
    path("create/", views.QuizCreateView.as_view(), name="quiz_quiz_create"),
    path("detail/<slug:slug>/", views.QuizDetailView.as_view(), name="quiz_quiz_detail"),
    path("update/<slug:slug>/", views.QuizUpdateView.as_view(), name="quiz_quiz_update"),
    path("start/<slug:slug>/", views.QuizStartView.as_view(), name="quiz_quiz_start"),
    path("active/<slug:slug>/", views.ActiveQuiz.as_view(), name="quiz_active_state_details"),
    path("active/<slug:slug>/control/", views.ActiveQuizControl.as_view(), name="quiz_active_state_control"),
    path("team/", views.TeamListView.as_view(), name="quiz_team_list"),
    path("team/create/", views.TeamCreateView.as_view(), name="quiz_team_create"),
    path("team/detail/<int:pk>/", views.TeamDetailView.as_view(), name="quiz_team_detail"),
    path("team/update/<int:pk>/", views.TeamUpdateView.as_view(), name="quiz_team_update"),
    # path("answer/", views.AnswerListView.as_view(), name="quiz_answer_list"),
    # path("answer/create/", views.AnswerCreateView.as_view(), name="quiz_answer_create"),
    # path("answer/detail/<int:pk>/", views.AnswerDetailView.as_view(), name="quiz_answer_detail"),
    # path("answer/update/<int:pk>/", views.AnswerUpdateView.as_view(), name="quiz_answer_update"),
    # path("round/", views.RoundListView.as_view(), name="quiz_round_list"),
    # path("round/create/", views.RoundCreateView.as_view(), name="quiz_round_create"),
    # path("round/detail/<int:pk>/", views.RoundDetailView.as_view(), name="quiz_round_detail"),
    # path("round/update/<int:pk>/", views.RoundUpdateView.as_view(), name="quiz_round_update"),
    # path("question/", views.QuestionListView.as_view(), name="quiz_question_list"),
    # path("question/create/", views.QuestionCreateView.as_view(), name="quiz_question_create"),
    # path("question/detail/<int:pk>/", views.QuestionDetailView.as_view(), name="quiz_question_detail"),
    # path("question/update/<int:pk>/", views.QuestionUpdateView.as_view(), name="quiz_question_update"),
)
