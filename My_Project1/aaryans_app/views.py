from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"todos.html",{'username' : 'Aaryan' ,'todos': [{'football': 'completed'}, {'django': 'pending'}]})
