from django.urls import path
from task.views import (
    stock_data_view,
    edit_stock_data_view,
    delete_stock_data_view,
    create_stock_data_view
)
app_name = 'task'

urlpatterns = [
    path('', stock_data_view, name='stock_data'),
    path('stock-data/<int:pk>/edit/', edit_stock_data_view, name='edit_stock_data'),
    path('stock-data/<int:pk>/delete/', delete_stock_data_view, name='delete_stock_data'),
    path('stock-data/create/', create_stock_data_view, name='create_stock_data'),
]
