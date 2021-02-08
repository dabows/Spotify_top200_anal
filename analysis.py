
'''


'''


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as ani

import bar_chart_race as bar


def countArtists():
    df = pd.read_csv('./products/all_df.csv')
    
    arts = df['Artist'].tolist()
    streams = df['Streams'].tolist()
    art_count = {}
    art_streams = {}

    for index, art in enumerate(arts):
        if not art in art_count:
            art_count[art] = 1
        else:
            art_count[art] += 1

        if not art in art_streams:
            art_streams[art] = streams[index]
        else:
            art_streams[art] += streams[index]
        
    df_art_cnt = pd.DataFrame(art_count.items(), columns=['Artist','Count'])
    df_art_strm = pd.DataFrame(art_streams.items(), columns=['Artist','Streams'])

    df_mgd = df_art_cnt.merge(df_art_strm, how='outer')
    
    df_mgd = df_mgd.sort_values(by='Streams', ascending=False)
    #df_mgd = df_mgd.sort_values(by='Count', ascending=False)
    #print(df_mgd.head(50))
    df_mgd.to_csv('./products/artist_count.csv')


def buildPlot(df1,i=int):
    
    p = plt.plot(df1.index, df1.values) #note it only returns the dataset, up to the point i
    
    
    

def aniGraph():
    df = pd.read_csv('./products/artist_streams_timeseries.csv', index_col=0)
    
    fig = plt.figure()

    #df.loc['1/1/2017'].sort_values(ascending=False)[:10].iloc[::-1].plot(kind='barh')

    #df['2017-01-01'].sort_values(ascending=0)[:10].plot(kind='bar')

    #animator = ani.FuncAnimation(fig, buildPlot(df), interval = 100)
    html = bar.bar_chart_race(df, figsize=(4, 2.5), title='COVID-19 Deaths by Country')
    HTML(html)
    
    plt.savefig('test.png', bbox_inches='tight')

if __name__ == '__main__':
    #countArtists()

    aniGraph()