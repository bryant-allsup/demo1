from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Creating a view for requesting hard drives
def index(request):
    #return HttpResponse("Homepage")
    #return render(request, 'index.html')
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'request.html')