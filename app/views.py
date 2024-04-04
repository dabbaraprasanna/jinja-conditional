from django.shortcuts import render

# Create your views here.
def loops(request):
    d={'name':'chitti'}
    return render(request,'loops.html',d)