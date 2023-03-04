from django.shortcuts import render
from .models import Feature
# Create your views here.
def index(request):
    feature=Feature()
    feature.id=1
    feature.name='Fast'
    feature.details='Our service is strongly quick'
    return render(request,'index.html', {'feature':feature})
def counter(request):
    words=request.POST['text']
    amount=len(words.split())
    return render(request,'counter.html',{'amount':amount})