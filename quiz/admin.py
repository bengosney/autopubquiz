from django.contrib import admin
from django import forms
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from . import models


class TeamAnswerAdminForm(forms.ModelForm):
    class Meta:
        model = models.TeamAnswer
        fields = "__all__"


class TeamAnswerAdmin(admin.ModelAdmin):
    form = TeamAnswerAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class TeamAdminForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = "__all__"


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = [
        "created",
        "last_updated",
        "name",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "name",
    ]


class AnswerAdminForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = "__all__"


class AnswerAdmin(admin.ModelAdmin):
    form = AnswerAdminForm
    list_display = [
        "answer",
        "correct",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "answer",
        "correct",
        "last_updated",
        "created",
    ]


class RoundAdminForm(forms.ModelForm):
    class Meta:
        model = models.Round
        fields = "__all__"


class RoundAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = RoundAdminForm
    list_display = [
        "last_updated",
        "created",
        "name",
        "position",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "name",
        "position",
    ]


class RoundInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Round


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = [
        "question",
        "last_updated",
        "position",
        "created",
    ]
    readonly_fields = [
        "question",
        "last_updated",
        "position",
        "created",
    ]


class QuestionInlineAdmin(admin.TabularInline):
    model = models.Question


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = "__all__"


class QuizAdmin(admin.ModelAdmin):
    # form = QuizAdminForm
    model = models.Quiz

    inlines = [
        RoundInlineAdmin,
    ]

    list_display = [
        "last_updated",
        "name",
        "slug",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "slug",
        "created",
        "opentdb_session_key",
    ]


class ActiveStateAdmin(admin.ModelAdmin):
    model = models.ActiveState


admin.site.register(models.ActiveState, ActiveStateAdmin)
admin.site.register(models.TeamAnswer, TeamAnswerAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.Round, RoundAdmin)
admin.site.register(models.Question, QuestionAdmin)
