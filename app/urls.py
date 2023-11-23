from django.urls import path

from .views import index, news

urlpatterns = [
    path('index/', index, name="index"),
    path('news/', news, name="news"),
    path('business/', news, name="business"),
    path('it/', news, name="it"),
    path('tech/', news, name="tech"),
]
