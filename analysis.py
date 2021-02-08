
'''
Shows top artist by appearances on top 200 as well
as top streams.

Also makes the vid.

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
    
    #df_mgd = df_mgd.sort_values(by='Streams', ascending=False)
    df_mgd = df_mgd.sort_values(by='Count', ascending=False)
    print(df_mgd.head(5))
    #df_mgd.to_csv('./products/artist_count.csv')

def aniGraph():
    df = pd.read_csv('./products/artist_streams_timeseries.csv', index_col=0)
    fig = plt.figure()

    #.iloc[::3, :] add to df to skip days
    bar.bar_chart_race(df, 'Racebar.mp4', figsize=(9,5), n_bars=5,
     fixed_max=True, period_length=150, steps_per_period=10, title='Spotify Top 5 Streams Per Day(Top 200 chart)')
    

if __name__ == '__main__':
    countArtists()

    #aniGraph()