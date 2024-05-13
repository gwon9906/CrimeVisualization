from django.contrib import admin
from django.urls import path
from crimes import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crimes/', views.index),
]
