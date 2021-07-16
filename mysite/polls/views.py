from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'blog.html', {'questions': questions})


def question_page(request, question_label):
    question_trouver = Question.objects.get(question_label__iexact=question_label)
    return render(request, 'question.html', {'question': question_trouver})
