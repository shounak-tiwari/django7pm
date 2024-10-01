from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def demo(request):
    return HttpResponse("Happy Home !")


def intro(request):
    x = input("Enter the input :")
    return HttpResponse("Hey! this is akash")


def html_file_fetch(request):
    return render(request,"index.html")

