from django.shortcuts import render
from django.core.paginator import Paginator
from task.models import StockData

def stock_data_view(request):
    all_stock_data = StockData.objects.all()
    items_per_page = 20
    paginator = Paginator(all_stock_data, items_per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request, 'task/home.html', {'page': page})

