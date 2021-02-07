
''' 
Turns all the csvs into one large dataframe and pickles it
'''

import os
from os import listdir
from os.path import isfile, join

import pandas as pd


def readCsv():
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
    df.to_csv('all_df.csv')


if __name__ == '__main__':
    readCsv()
