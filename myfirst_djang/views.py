#I have created this one-Shreya
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'Shreya','place':'NOrevealofpersonalinfo'}
    return render(request,'index.html',params)
def about(request):
    params={'ooh':'oooh'}
    return render(request,'about.html',params)
def contact(request):
    params={'ooh':'oooh'}
    return render(request,'contact.html',params)

# def about(request):
#     return HttpResponse("<h1>this is totally about learning django</h1>")
# def read_file(request):
#     with open('myfirst_djang/one.txt','r') as f:
#         st=f.read()
#         return HttpResponse(st)
def analyse(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newLine=request.GET.get('newLine','off')
    extraSpace=request.GET.get('extraSpace','off')
    charCount=request.GET.get('charCount','off')

    #print(djtext)
    #analysed=djtext
    punctuations='''!@#$%^&*():;'""<>,./?{}[]\`~'''
    analysed=""
    if(removepunc=="on"):
        for char in djtext:
            if char not in punctuations:
                analysed+=char
        params={'purpose':'Remove Punctuation','analysed_text':analysed}
        return render(request,'analyse.html',params) 
    if(fullcaps=="on"):
        for char in djtext:
            analysed=analysed+char.upper()
        params={'purpose':'Full Caps','analysed_text':analysed}
        return render(request,'analyse.html',params)
    if(newLine=="on"):
        for char in djtext:
            if(char!='\n'):
                analysed=analysed+char
        params={'purpose':'NewLine Remover','analysed_text':analysed}
        return render(request,'analyse.html',params)
    if(extraSpace=="on"):
        for i,char in enumerate(djtext):
            if(djtext[i]==" " and djtext[i+1]==" "):
                pass
            else:
                analysed=analysed+char
        params={'purpose':'NewLine Remover','analysed_text':analysed}
        return render(request,'analyse.html',params)
    if(charCount=="on"):
        c=0;
        for char in djtext:
            if(char==" "):
                pass
            else:
            
                c=c+1
        params={'purpose':'Full Caps','analysed_text':c}
        return render(request,'analyse.html',params)
    
     
    else:
        return HttpResponse("Error")
        





     
     
  
# def Capitalise(request):
#     return HttpResponse("I capitalise  <br> <a href=http://127.0.0.1:8000/>click here to get surprised</a>")
# def Newline(request):
#     return HttpResponse("I remove newline  <br> <a href=http://127.0.0.1:8000/>click here to get surprised</a>")
# def SpaceRemove(request):
#     return HttpResponse("I remove all the spaces  <br> <a href=http://127.0.0.1:8000/>click here to get surprised</a>")
