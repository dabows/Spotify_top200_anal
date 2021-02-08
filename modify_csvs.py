
''' 
Turns all the csvs into one large dataframe and saves it
'''

import os
from os import listdir
from os.path import isfile, join

import pandas as pd


def allCsv():
    data_path = './csvs/'
    fname_list = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    df = pd.DataFrame()

    for f in fname_list:
        print(f)

        df2 = pd.read_csv(data_path+f)

        date = [f[:10] for i in range(len(df2))] #create column of dates
        df2['Date'] = date
        
        df = pd.concat([df,df2], ignore_index=True, sort=False)

    df = df.drop(['URL'], axis=1)
    df.to_csv('./products/all_df.csv')

def timeseriesCsv():
    df = pd.read_csv('./products/all_df.csv')
    arts = []
    tmp = df['Artist'].to_list()
    [arts.append(a) for a in tmp if a not in arts]
    
    dates = []
    tmp = df['Date'].to_list()
    [dates.append(a) for a in tmp if a not in dates]
    
    df_ts = pd.DataFrame(columns=arts, index=dates)
    df_ts = df_ts.fillna(0)

    for index, row in df.iterrows():
        print(row['Date'])
        df_ts.loc[row['Date'], row['Artist']] += row['Streams']

    print(df_ts)
    df_ts.to_csv('./products/artist_streams_timeseries.csv')


if __name__ == '__main__':
    #readCsv()
    timeseriesCsv()
