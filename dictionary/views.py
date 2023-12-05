from django.shortcuts import render

  # Create your views here.

def HomeView(request):
    return render(request, 'dictionary/home.html')

def SearchView(request):
    return render(request, 'dictionary/search.html')
