# myfile
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # sending variables to templates with params
    params = {'name': 'Priya', 'country': 'India'}

    return render(request, 'index.html', params)


def analyze(request):
    # GET.get returns text in input area or form otherwise takes default
    djtext = (request.POST.get('text', 'default'))

    # check checkbox values
    removepunc = (request.POST.get('removepunc', 'off'))
    capitalize = (request.POST.get('capitalize', 'off'))
    newlinerem = (request.POST.get('newlinerem', 'off'))
    exspacerem = (request.POST.get('exspacerem', 'off'))
    charcount = (request.POST.get('charcount', 'off'))

    # to check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-{}[];:'"\,<>/.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlinerem == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":  # CARRIAGE RETURN \r
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if exspacerem == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and capitalize != "on" and newlinerem != "on" and exspacerem != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)


def aboutus(request):
    return render(request, 'aboutus.html')
