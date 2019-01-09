import django_tables2 as tables
from .models import Biodata

class BiodataTable(tables.Table):
    class Meta:
        model = Biodata