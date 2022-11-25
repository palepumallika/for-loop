from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':250,'b':500,'c':200}
    return render(request,'a2_first.html',d)
def a2_second(request):
    d={'name':'mallika'}
    return render(request,'a2_second.html',d)

