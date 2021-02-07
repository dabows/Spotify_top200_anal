
"""
Download all available csv's
from https://spotifycharts.com/regional, must use link
from latest date ex:

https://spotifycharts.com/regional/global/daily/2021-02-06/Download

"""

import os
from multiprocessing import Pool

import requests
from datetime import date, timedelta


def getDate(dt):
    return dt - timedelta(days=1)

def getdateList():
    dt = date.today()
    dt_list = []
    while(not str(dt) == '2017-01-01'): #hardcoded date for first spotify top chart
        dt = getDate(dt)
        dt_list.append(dt)

    return dt_list

def download(dt):
    CSV_URL = f'https://spotifycharts.com/regional/global/daily/{dt}/download'
    try:
        with open(f'./csvs/{dt}.csv', 'wb') as f, \
            requests.get(CSV_URL, stream=True) as r:
            for line in r.iter_lines():
                if 'Note that th' in str(line): continue
                f.write(line+'\n'.encode())
    except:
        print(dt)
        
if __name__ == '__main__':
    dt_list = getdateList()

    with Pool(16) as p:
        download(p.map(download, dt_list))