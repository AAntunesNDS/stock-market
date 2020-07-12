import sys
import pandas as pd
import stock_service as sv
import json

def load_data_btc(json_all_days, coin : str):
    data_for_all_days = pd.read_json(json
    .dumps(json_all_days, ensure_ascii=False))\
    .T
    
    CYN_cols = [col for col in data_for_all_days.columns if 'CNY' in col]
    USD_cols = [col for col in data_for_all_days.columns if 'USD' in col]
    
    df = data_for_all_days[CYN_cols]
    if coin == 'USD':
        df = data_for_all_days[USD_cols]
    
    return df
    
    
def transform_in_fourcolumns(df):
    columns = df.columns.tolist()
    df.drop(df.columns[[4]], axis=1, inplace=True)
    rename_dict = {
        columns[0] : 'open',
        columns[1] : 'high', 
        columns[2] : 'low',
        columns[3] : 'close'
    }
    df.rename(columns=rename_dict, inplace=True)
    return df

if __name__ == "__main__":
        
    print(json.dumps(sv.run()['meta_data'], indent=4))
    '''
    {
        "1. Information": "Daily Prices and Volumes for Digital Currency",
        "2. Digital Currency Code": "BTC",
        "3. Digital Currency Name": "Bitcoin",
        "4. Market Code": "CNY",
        "5. Market Name": "Chinese Yuan",
        "6. Last Refreshed": "2020-07-12 00:00:00",
        "7. Time Zone": "UTC"
    }
    '''
    df = load_data_btc(sv.run()['data_for_all_days'], 'USD')
    df = transform_in_fourcolumns(df)
    print(df)
    '''
                open     high      low    close
    2020-07-12  9234.02  9268.52  9230.61  9259.99
    2020-07-11  9288.34  9299.28  9178.25  9234.03
    2020-07-10  9232.42  9317.48  9125.00  9288.34
    2020-07-09  9436.06  9440.79  9160.00  9232.43
    2020-07-08  9257.40  9470.00  9231.00  9436.06
    ...             ...      ...      ...      ...
    2017-10-21  6013.72  6171.00  5850.03  6024.97
    2017-10-20  5683.31  6110.00  5600.00  6010.01
    2017-10-19  5513.00  5710.00  5490.26  5683.90
    2017-10-18  5595.00  5596.00  5037.95  5512.06
    2017-10-17  5760.00  5774.98  5508.63  5595.00
    '''

