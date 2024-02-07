import json
from .models import StockData  

def load_json_data_to_sql():
    file_path = 'task/stock_market_data.json'  
    with open(file_path, 'r') as f:
        json_data = json.load(f)

    for item in json_data:
        item['high'] = float(item['high'].replace(',', ''))
        item['low'] = float(item['low'].replace(',', ''))
        item['open'] = float(item['open'].replace(',', ''))
        item['close'] = float(item['close'].replace(',', ''))
        item['volume'] = int(item['volume'].replace(',', ''))
        
        data_instance = StockData(
            date=item['date'],
            trade_code=item['trade_code'],
            high=item['high'],
            low=item['low'],
            open=item['open'],
            close=item['close'],
            volume=item['volume']
        )
        
        data_instance.save()
