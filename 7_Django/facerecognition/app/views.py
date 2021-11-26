from django.shortcuts import render
from django.http import HttpResponse
from app.forms import FaceRecognitionform
# Create your views here.


def index(request):
    form = FaceRecognitionform()
    
    if request.method == 'POST':
        form =  FaceRecognitionform(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit =True)
    
    
    return render(request,'index.html',{'form':form})