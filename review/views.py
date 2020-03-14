from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = "review/index.html"
    return render(request, template_name)

def chap1(request):
    template_name = "review/chap1.html"
    return render(request, template_name)

def chapter(request,pk):
    template_name = "review/chapterHTML/"+str(pk)+".html"
    return render(request, template_name)

def viewFunction(request, i):
    template_name = ""

def zero(request):
    template_name = "review/chapterHTML/0.html"
    return render(request, template_name)