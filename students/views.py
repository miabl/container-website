# Create your views here.
from django.shortcuts import render, redirect
from .forms import NewUserForm


def register(response):
    if response.method == 'POST':
        form = NewUserForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = NewUserForm()

    return render(response, 'registration/register.html', {'form': form})
