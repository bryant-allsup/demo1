from django.shortcuts import render
from django.http import HttpResponse

# Creating a view for requesting hard drives
def index(request):
    return HttpResponse("May I request, for hard drives")