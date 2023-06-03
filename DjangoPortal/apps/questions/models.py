from django.db import models

choices = [
    ('Финансы', 'Финансы'),
    ('Продажи', 'Продажи'),
    ('Маркетинг', 'Маркетинг')
]


# Create your models here.

class Question(models.Model):
    question_formulation = models.CharField('Формулировка вопроса:', max_length=200)
    question_answer = models.CharField('Ответ на вопрос:', max_length=200)
    question_theme = models.CharField('Тема вопроса:', choices=choices, max_length=200)

    def __str__(self):
        return self.question_theme

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
