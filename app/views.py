from django.shortcuts import render
from app.forms import *
from app.models import *

# Create your views here.

def i_topic(request):
    TOD=TopicForm()
    d={'TOD':TOD}
    if request.method=='POST':
       FTD= TopicForm(request.POST)
       if FTD.is_valid():
           topic_name=request.POST['topic_name']
           TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
           TO.save()

           RTO=Topic.objects.all()
           d1={"RTO":RTO}
           return render(request,'display.html',d1)
    return render(request,'wtopic.html',d)

def i_webpage(request):
    WOD=WebPageForm()
    d={'WOD':WOD}
    return render(request,'wwebpage.html',d)