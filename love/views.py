from django.shortcuts import render

# Create your views here.

def cherry(request):
    return render(request,'cherry.html')


def devi(request):
    return render(request,'devi.html')