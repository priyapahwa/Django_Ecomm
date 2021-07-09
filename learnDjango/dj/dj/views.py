# myfile
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # sending variables to templates with params
    params = {'name': 'Priya', 'country': 'India'}

    return render(request, 'index.html', params)
    # return HttpResponse('''<h1>Welcome</h1> <a href="https://www.youtube.com/"> Youtube </a>
    # <a href="https://www.google.com/"> Google </a>''')


def about(request):
    return HttpResponse("Hey")
