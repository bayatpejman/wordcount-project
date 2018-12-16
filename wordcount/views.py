
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def countwords(request):
    ft=request.GET['fulltext']
    wl=ft.split()
    w=len(wl)
    worddic={}
    for word in wl:
        if word in worddic:
            #increament
            worddic[word]+=1
        else:
            #add to dictionary
            worddic[word]=1

    sorteddict= sorted(worddic.items(),key=operator.itemgetter(1), reverse=True)

    return render(request,'counts.html',{'fulltext':ft,'word':w,'worddic':sorteddict})
