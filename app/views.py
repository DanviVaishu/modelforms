from django.shortcuts import render
from django.http import HttpResponse
from app.forms import*
def Insert_Topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data inserted successfully')
    return render(request,'Insert_Topic.html',d)
def Insert_Webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('data inserted successfully')
    return render(request,'Insert_Webpage.html',d)

def Insert_Access_Record(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('data inserted successfully')
    return render(request,'Insert_Access_Record.html',d)