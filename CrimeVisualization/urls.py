from django.contrib import admin
from django.urls import path
from crimes import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('crimes/', include('crimes.urls')),
]
