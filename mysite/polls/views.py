from django.shortcuts import render, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'blog.html', {'questions': questions})


def question_page(request, question_label):
    # question_label correspond a l'entree url pour la question choisie
    question_trouver = Question.objects.get(question_label__iexact=question_label)
    return render(request, 'question.html', {'question': question_trouver})


@login_required(login_url="/accounts/login")
def question_create(request):
    if request.method == 'POST':
        form = forms.CreateQuestion(request.POST, request.FILES)
        if form.is_valid():
            # save question to DB
            instance = form.save(commit=False)
            instance.auteur = request.user
            instance = form.save()
            return redirect('blog:index')
    else:
        form = forms.CreateQuestion()
    return render(request, 'userview.html', {'form': form})
