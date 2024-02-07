from django.urls import path
from task.views import stock_data_view

urlpatterns = [
    path('stock-data/', stock_data_view, name='stock_data'),
]