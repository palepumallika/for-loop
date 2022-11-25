from django.shortcuts import render

# Create your views here.
def a1_first(request):
    return render(request,'a1_first.html')
def a1_second(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'a1_second.html',d)
