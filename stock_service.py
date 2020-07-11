import requests

API_KEY = 'demo'
SYMBOL_BTC = 'BTC'
MARKET_CNY = 'CNY'
BASE_ADDRESS = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={SYMBOL_BTC}&market={MARKET_CNY}&apikey=demo'

#TODO make async for each label symbol
def get_time_series(link_request: str, API_KEY):
    request_obj = requests.get(link_request + API_KEY)
    if (request_obj.status_code == 200):
        json_obj = request_obj.json()
        meta_data = json_obj['Meta Data']
        data_for_all_days = json_obj['Time Series (Digital Currency Daily)']
    
    response = dict(
        meta_data = meta_data,
        data_for_all_days = data_for_all_days
    )

    return response

def run():
    #TODO iterate over a list of symbols keeping base address
    return get_time_series(BASE_ADDRESS, API_KEY)

if __name__ == "__main__":
    print(run()['meta_data'])
