from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        # check if user input is valid
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
