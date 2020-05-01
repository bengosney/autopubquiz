import time
from pprint import pprint
import random
import requests
import urllib.parse
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Quiz(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    opentdb_session_key = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("quiz_quiz_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("quiz_quiz_update", args=(self.slug,))

    def get_start_url(self):
        return reverse("quiz_quiz_start", args=(self.slug,))

    @property
    def start_url(self):
        return self.get_start_url()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

            args = {
                'command': 'request'
            }
            response = requests.get('https://opentdb.com/api_token.php', params=args)
            response.raise_for_status()
            jsonResponse = response.json()
            pprint(jsonResponse)
            self.opentdb_session_key = jsonResponse['token']

        super().save(*args, **kwargs)


class TeamAnswer(models.Model):
    # Relationships
    answer = models.ForeignKey("quiz.answer", on_delete=models.CASCADE)
    team = models.ForeignKey("quiz.team", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("quiz_teamanswer_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("quiz_teamanswer_update", args=(self.pk,))


class Team(models.Model):
    # Relationships
    quiz = models.ForeignKey("quiz.quiz", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("quiz_team_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("quiz_team_update", args=(self.pk,))


class Answer(models.Model):
    # Relationships
    question = models.ForeignKey("quiz.question", on_delete=models.CASCADE)

    # Fields
    answer = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("quiz_answer_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("quiz_answer_update", args=(self.pk,))


class Round(models.Model):
    CATEGORIES = [
        (0, "Any Category"),
        (9, "General Knowledge"),
        (10, "Entertainment: Books"),
        (11, "Entertainment: Film"),
        (12, "Entertainment: Music"),
        (13, "Entertainment: Musicals & Theatres"),
        (14, "Entertainment: Television"),
        (15, "Entertainment: Video Games"),
        (16, "Entertainment: Board Games"),
        (17, "Science & Nature"),
        (18, "Science: Computers"),
        (19, "Science: Mathematics"),
        (20, "Mythology"),
        (21, "Sports"),
        (22, "Geography"),
        (23, "History"),
        (24, "Politics"),
        (25, "Art"),
        (26, "Celebrities"),
        (27, "Animals"),
        (28, "Vehicles"),
        (29, "Entertainment: Comics"),
        (30, "Science: Gadgets"),
        (31, "Entertainment: Japanese Anime & Manga"),
        (32, "Entertainment: Cartoon & Animations"),
    ]

    ANY_DIFFICULTY = None
    EASY_DIFFICULTY = 'easy'
    MEDIUM_DIFFICULTY = 'medium'
    HARD_DIFFICULTY = 'hard'
    DIFFICULTY_CHOICES = [
        (ANY_DIFFICULTY, 'Any'),
        (EASY_DIFFICULTY, 'Easy'),
        (MEDIUM_DIFFICULTY, 'Medium'),
        (HARD_DIFFICULTY, 'Hard')
    ]

    # Relationships
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    difficulty = models.CharField(max_length=255, choices=DIFFICULTY_CHOICES, default=ANY_DIFFICULTY)
    question_count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("`quiz_round_detail`", args=(self.pk,))

    def get_update_url(self):
        return reverse("quiz_round_update", args=(self.pk,))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.populateQuestion()

    def populateQuestion(self):
        needed_count = self.question_count - self.question_set.count()
        if needed_count > 0:
            args = {
                'amount': needed_count,
                'category': self.category,
                'difficulty': self.difficulty,
                'encode': 'url3986',
                'token': self.quiz.opentdb_session_key,
            }
            response = requests.get('https://opentdb.com/api.php', params=args)
            response.raise_for_status()
            jsonResponse = response.json()
            print("adding more questions")

            for q in jsonResponse['results']:
                question = Question()
                question.round = self
                question.question = urllib.parse.unquote(q['question'])
                if q['type'] == "boolean":
                    question.question = f"True or false, {question.question}"
                question.save()

                answers = []
                answer = Answer()
                answer.question = question
                answer.answer = urllib.parse.unquote(q['correct_answer'])
                answer.correct = True
                answers.append(answer)
                for a in q['incorrect_answers']:
                    answer = Answer()
                    answer.question = question
                    answer.answer = urllib.parse.unquote(a)
                    answers.append(answer)

                random.shuffle(answers)
                for a in answers:
                    a.save()


class Question(models.Model):
    # Relationships
    round = models.ForeignKey("quiz.round", on_delete=models.CASCADE)

    # Fields
    question = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    position = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("quiz_question_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("quiz_question_update", args=(self.pk,))


class ActiveState(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def round_limit(self):
        return self.quiz

    class Meta:
        pass

    def __str__(self):
        return f"{self.quiz.name} - {self.created}"

    def get_absolute_url(self):
        return reverse("quiz_active_state_details", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(f"{self.quiz.name} {time.time()}")

        return super().save(*args, **kwargs)
