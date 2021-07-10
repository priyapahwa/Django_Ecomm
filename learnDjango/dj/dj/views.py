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
    # GET.get returns text in input area or form otherwise takes default
    djtext = (request.GET.get('text', 'default'))

    # check checkbox values
    removepunc = (request.GET.get('removepunc', 'off'))
    capitalize = (request.GET.get('capitalize', 'off'))
    newlinerem = (request.GET.get('newlinerem', 'off'))

    # to check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-{}[];:'"\,<>/.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'about.html', params)

    elif capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'about.html', params)

    else:
        return HttpResponse("Error")
