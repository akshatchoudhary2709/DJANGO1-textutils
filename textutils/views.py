## I have created this file----Akshat

from django.http import HttpResponse
from django.shortcuts import render
import requests
#
def index(request):
    return HttpResponse("hello world")
#
# def about(request):
#     return HttpResponse("greetings from AK")
#
# def urls(request):
#     return HttpResponse('''<a href='https://webbyaks.000webhostapp.com/donation/donation/main1.html'>Mine website</a>''')


# def removepunc(request):
#     # get the text
#     # analyse the text
#     djtext=print(request.GET.get('text','default'))
#     print(djtext)
#     return HttpResponse("Remove punctuation")
# def capitalize(request):
#     return HttpResponse("Capitalize the word")
#
# #templates
#
def main(request):
    #params={'name':'Amazing27','place':'India'}
    return render(request,'index.html')

def analyze(request):
    # get the text
    # analyse the text
    djtext=request.POST.get('text','default')

    # checkbox checking
    removepunc =request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')
    space_remover = request.POST.get('space_remover', 'off')
    character_counter = request.POST.get('character_counter', 'off')
    # print(djtext)
    # print(removepunc)
    #return HttpResponse("Remove punctuation")
    #analyzed=djtext
    analyzed=""
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char


        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'Change in Uppercase', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed

    if(new_line_remover=="on"):
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'New Line Removal','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
        djtext=analyzed

    if (space_remover == "on"):
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Space Removal', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed

    if (character_counter == "on"):
        lst=[]
        for char in djtext:
            lst.append(char)
        analyzed="The length of given text is:"+str(len(lst))




        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)



    # else:
    #     return HttpResponse("Error")



    if (removepunc!="on" and fullcaps!="on" and new_line_remover!="on" and space_remover != "on" and character_counter != "on"):
        return HttpResponse("SELECT ANY PARTICULAR OPERATION TO PERFORM")

    return render(request, 'analyze.html', params)