from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def news(request):
    return render(request, "app/news.html")
