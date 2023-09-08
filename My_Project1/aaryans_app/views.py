from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"todos.html",{'username' : 'AaryanAA' ,'todos': [{'football': 'completed'}, {'django': 'pending'}]})
