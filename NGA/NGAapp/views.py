from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')


def board(request):
    return render(request, 'board.html')
