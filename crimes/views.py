from django.shortcuts import render
from .models import Crime
from collections import Counter


def crime_chart(request):
    data = Crime.objects.all()
    categories = Counter([crime.category for crime in data])
    categories = sorted(categories.items())
    return render(request, 'crimes/chart.html', {'categories': categories})

from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
