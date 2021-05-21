
from django.http import HttpResponse
from django.shortcuts import render
# def ab(request):
#     return HttpResponse("hello")
def index(request):
    return render(request,'web2.html')
# def frm(request):
#     dj=request.GET.get('text','default')
#     return HttpResponse("test complete")
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if  char != '\n' and char!='\r':
                analyzed = analyzed + char
        # print(analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text':analyzed}
        # Analyze the text
        djtext=analyzed
    
    return render(request, 'remover2.html', params)
