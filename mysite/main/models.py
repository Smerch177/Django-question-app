from mysite.settings import TEMPLATES
from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz = models.TextField('Quiz', null=False)
    answer = models.BooleanField('Answer', default=True)

    def __repr__(self) -> str:
         return f'{self.quiz}'

    def __str__(self) -> str:
        return self.quiz

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = "Quiz's"
