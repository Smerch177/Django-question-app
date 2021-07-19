from functools import reduce
from typing import Counter
from django.shortcuts import redirect, render
from requests.api import request
from .models import Quiz
from .forms import BoolForm, QuizForm
import requests
from random import sample

# Create your views here.
def index(request):
    if request.user.is_superuser:
        return render(request, 'index_admin.html')
    else:
        return render(request, 'index.html')

def quiz_make(request):
    return render(request, 'quiz_make.html', {'form' : QuizForm})

def quiz_create(request):
    if request.POST:
        quiz = Quiz()
        quiz.quiz = request.POST['quiz']
        quiz.answer = request.POST['answer']
        quiz.save()
    return redirect('/')

def quiz_create_random(request):
    response = requests.get('https://opentdb.com/api.php?amount=3&type=boolean')
    data = response.json()
    for el in data['results']:
        quiz = Quiz()
        el_quiz = el['question'].replace('&#039;',"'")
        el_quiz = el_quiz.replace('&quot;','"')
        quiz.quiz = el_quiz
        quiz.answer = el['correct_answer']
        quiz.save()
    return redirect('/')

def quiz(request):
    data = []
    quiz = list(Quiz.objects.all())
    quiz = sample(quiz,3)
    for i in range(3):
        data_old = {f'form' : BoolForm(prefix=i), f'quiz': quiz[i]}
        data.append(data_old)
    return render(request, 'quiz.html', {'data': data})

def quiz_answer(request):
    if request.POST:
        counter = 0 
        quiz0 = Quiz.objects.get(quiz=request.POST['question_0'])
        quiz1 = Quiz.objects.get(quiz=request.POST['question_1'])
        quiz2 = Quiz.objects.get(quiz=request.POST['question_2'])
        if request.POST['user_choice'] == str(quiz0.answer):
            counter += 1
        if request.POST['1-user_choice'] == str(quiz1.answer):
            counter += 1
        if request.POST['2-user_choice'] == str(quiz2.answer):
            counter += 1
        if counter == 3:
            return render(request, 'answer_win.html')
        else:
            return render(request, 'answer.html', {'ammount': counter})