from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Biodata


def profile(request):
    all_info = Biodata.objects.all()
    template = loader.get_template("gallery/biodata.html")

    context = {
        'all_info' : all_info
    }
        
    return HttpResponse(template.render(context, request))

    