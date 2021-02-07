
'''


'''


import pandas as pd

import squarify
import matplotlib.pyplot as plt


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

def aniGraph():
    df = pd.read_csv('./products/artist_count.csv')

if __name__ == '__main__':
    #countArtists()

    aniGraph()