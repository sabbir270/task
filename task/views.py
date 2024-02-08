from django.core.paginator import Paginator
from task.models import StockData
from django.shortcuts import render, redirect, get_object_or_404
from task.forms import StockDataForm
import plotly.graph_objects as go



def stock_data_view(request):
    all_stock_data = StockData.objects.order_by('date').all()
    items_per_page = 20
    paginator = Paginator(all_stock_data, items_per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    dates = [data.date for data in all_stock_data]
    close_values = [data.close for data in all_stock_data]
    volumes = [data.volume for data in all_stock_data]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dates, y=close_values, mode='lines', name='Close Value'))
    fig.add_trace(go.Bar(x=dates, y=volumes, name='Volume', yaxis='y2'))

    fig.update_layout(
        title='Line and Bar Chart - Close Value and Volume',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Close Value'),
        yaxis2=dict(title='Volume', overlaying='y', side='right'),
        legend=dict(x=0, y=1, traceorder='normal', font=dict(size=12)),
        margin=dict(l=50, r=50, t=50, b=50),
        height=600
    )
    
    chart = fig.to_html()
    context = {
        'page': page,
        'chart': chart
    }
    return render(request, 'task/home.html', context)


def edit_stock_data_view(request, pk):
    stock_data = get_object_or_404(StockData, pk=pk)
    if request.method == 'POST':
        form = StockDataForm(request.POST, instance=stock_data)
        if form.is_valid():
            form.save()
            return redirect('task:stock_data')
    else:
        form = StockDataForm(instance=stock_data)
    return render(request, 'task/edit_stock_data.html', {'form': form})


def delete_stock_data_view(request, pk):
    stock_data = get_object_or_404(StockData, pk=pk)
    if request.method == 'POST':
        stock_data.delete()
        return redirect('task:stock_data')
    return render(request, 'task/delete_stock_data.html', {'stock_data': stock_data})


def create_stock_data_view(request):
    if request.method == 'POST':
        form = StockDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:stock_data') 
    else:
        form = StockDataForm()
    return render(request, 'task/create_stock_data.html', {'form': form})


