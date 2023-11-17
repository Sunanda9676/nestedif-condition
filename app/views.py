from django.shortcuts import render

# Create your views here.
def nestedcondition(request):
    d={'a':30,'b':46,'c':52}
    return render(request,'nestedcondition.html',d)
