import schedule, time, requests

def hello_world():
    print(f"Hello World {time.ctime()}")

def backend_16_1b():
    print(f"Здравствуйте, сегодня у вас урок в 19:00")

# schedule.every().monday.at("19:56").do(backend_16_1b)
# schedule.every(5).seconds.do(hello_world)
# schedule.every(1).minutes.do(hello_world)
# schedule.every().day.at('19:47').do(hello_world)
# schedule.every().monday.at('19:49').do(hello_world)
# schedule.every().day.at("19:52", "Asia/Bishkek").do(hello_world)

def get_btc_price():
    response = requests.get('https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    data = response.json()
    price = data['price']
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"Цена биткоина на {current_time}: {price}$")

schedule.every(1).seconds.do(get_btc_price)

def get_eth_price():
    response = requests.get('https://www.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
    data = response.json()
    price = data['price']
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"Цена ETH на {current_time}: {price}$")

schedule.every(1).second.do(get_eth_price)

while True:
    schedule.run_pending()
    time.sleep(1)