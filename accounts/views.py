# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  # 회원가입 후 리디렉션할 URL
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
