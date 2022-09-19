from django.shortcuts import render
from mywatchlist.models import MyWatchListItem

# TODO: Create your views here.
def show_mywatchlist(request):
    mywatchlist_item = MyWatchListItem.objects.all()
    context = {
        'list_barang': mywatchlist_item,
        'nama': 'Kathleen Daniella Wijaya',
        'student_id': '2106637366'
    }
    return render(request, "mywatchlist.html", context)
