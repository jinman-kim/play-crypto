from binance.client import Client
from datetime import datetime, timedelta
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET') 


def _date_shifter():  # 날짜 변환기 (binance_api 규격) ->  날짜 월, 연도 (1 JAN, 2023)
    
    today = datetime.today()
    yesterday = today + timedelta(days=-1)
    btc_yesterday, btc_today = yesterday.strftime("%d %B, %Y"), today.strftime("%d %B, %Y")
    
    return btc_yesterday, btc_today


def _binance_crawl(client: Client, 
                   intervals, 
                   yesterday: _date_shifter()[0], 
                   today: _date_shifter()[1]):

    for interval in intervals:
        klines = client.get_historical_klines('BTCUSDT', 
                                              getattr(Client, f"KLINE_INTERVAL_{interval}"), 
                                              yesterday, 
                                              today)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
                                            'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignored'])
        df = df.iloc[:,:6]
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        file_name = datetime.today().strftime('%Y-%m-%d')
        folder_path = './data'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        df.to_csv(os.path.join(folder_path, f'BTCUSDT-{file_name}.csv'), index=False)

        
yesterday, today = _date_shifter()
client = Client(api_key, api_secret)
intervals = ['1MINUTE']
_binance_crawl(client, intervals, yesterday, today)


file_name = 'BTCUSDT-' + datetime.today().strftime('%Y-%m-%d')
btc_data = pd.read_csv(f'./data/{file_name}.csv')
# BTCUSDT-2023-07-19
print(btc_data.columns)
