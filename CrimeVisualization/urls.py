from django.contrib import admin
from crimes.views import search_crime_data_view
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('crimes/', include('crimes.urls')),
    path('crime_map/', include('crime_map.urls')),
    path('', search_crime_data_view, name='home'),  # 홈 화면을 검색 뷰로 설정
]
