from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            print(request.POST['task'])
    return render(request, 'index.html')
