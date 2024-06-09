# accounts/views.py

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  # 회원가입 후 리디렉션할 URL
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

class LoginView(auth_views.LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
