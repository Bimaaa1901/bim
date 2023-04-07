import pandas as pd
import talib
import ccxt
import time

while True:
    # Load historical price data from exchange
    #exchange = ccxt.binance()
    #exchange = ccxt.coinbasepro()
    exchange = ccxt.okex()
    symbol = 'BTC/USDT'
    timeframe = '1d'
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.set_index('timestamp')

    # Calculate EMA 20
    ema_20 = talib.EMA(df['close'], timeperiod=20)

    # Calculate Bollinger Bands
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod=20)

    # Get the last values of EMA 20, SMA 9, and Bollinger Bands
    ema_20_last = ema_20.iloc[-1]
    upper_last = upper.iloc[-1]
    middle_last = middle.iloc[-1]
    lower_last = lower.iloc[-1]

    # Get the last close price
    last_price = df['close'].iloc[-1]

    # Menghitung jarak antara Upper Bollinger Band dengan harga BTC dalam persentase
    #distance_from_upper_band = ((upper_last - last_price) / upper_last) * 100
    distance_from_upper_band = ((last_price - upper_last) / last_price) * 100

    # Print the last values of EMA 20, SMA 9, Bollinger Bands, and close price
    print('BTC/IDR Price:', last_price)
    print('EMA 20:', ema_20_last)
    print('Upper Bollinger Band:', upper_last)
    print('Middle Bollinger Band:', middle_last)
    print('Lower Bollinger Band:', lower_last)
    print('Distance from Upper Bollinger Band (%):', distance_from_upper_band)
    time.sleep(2)
