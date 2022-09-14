from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    catalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': catalog_item,
        'nama': 'Kathleen',
        'student_id': '2106637366'
    }
    return render(request, "katalog.html", context)
