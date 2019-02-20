from django.shortcuts import render
from appTwo.models import User
from . import forms
# Create your views here.


def index(request):
    users = User.objects.order_by('dob')
    return render(request, 'appTwo/index.html', {'users':users})


def users(request):

    form = forms.Signup()

    if request.method == 'POST':
        form = forms.Signup(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            user = User(name=name, email=email, dob=dob)
            user.save()

    return render(request, 'appTwo/users.html', {'form': form})

def details(request):
    users = User.objects.order_by('dob')

    return render(request, 'appTwo/details.html', {'users':users})