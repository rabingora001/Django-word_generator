from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if "attempt" not in request.session:
        request.session['attempt'] = 0
    unique_id = get_random_string(length=14)
    request.session['word']=unique_id
    return render(request, 'words/index.html')

def create(request):
    request.session['attempt'] +=1
    return redirect('/')


def delete(request):
    request.session.clear()
    return redirect('/')




