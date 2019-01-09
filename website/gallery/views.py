from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Biodata
from .tables import BiodataTable


def profile(request):
    table = BiodataTable(Biodata.objects.all())

    return render(request, 'gallery/biodata.html', {'table' : table})

    