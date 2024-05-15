from django.contrib import admin
from django.urls import path
from crimes import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crimes/', include('crimes.urls')),
    path('board/', include('board.urls')),
]
