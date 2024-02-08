from django import forms
from .models import StockData

class StockDataForm(forms.ModelForm):
    class Meta:
        model = StockData
        fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']
