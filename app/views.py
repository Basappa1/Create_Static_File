from django.shortcuts import render

# Create your views here.


def img1(request):
    return render(request,'img1.html')

def img2(request):
    return render(request,'img2.html')