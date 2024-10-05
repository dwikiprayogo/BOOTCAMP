import mysql.connector as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
from urllib.error import URLError
from babel.numbers import format_currency
from numerize import numerize
from helper import generate_wordcloud, add_logo

import plotly.express as px

st.set_page_config(page_title="Analisa Kandidat Bootcamp Influenser 2024",
                   page_icon="📈",
                   layout="wide")

# hide menu style
style = """
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

<style>
"""
# st.markdown(style, unsafe_allow_html=True)



db_connection = sql.connect(host='10.240.20.20', database='test', user='staff', password='6tQiQkNu42', port='8807')
# DEFINISIKAN DATA DAN METRIKS
df = pd.read_sql('SELECT * FROM bootcamp_users', con=db_connection)
data = pd.read_csv('data/labeled.csv').drop(['Unnamed: 0'], axis=1)
data['like'] = data['like'].replace({'undefined':0}).astype(int)
data['time'] = data['time'].apply(lambda x: x[:10])
data['interaction'] = data.apply(lambda x: x['like']+x['reply']+x['retweet'], axis=1)

# FOR SENTIMENT
df_sentiment = pd.DataFrame(data['prediction'].value_counts()).rename({'prediction':'total',
                                                                       'count':'total'}, axis=1)
# df_sentiment.columns = [['total', df_sentiment.columns[-1]]]
df_sentiment['sentiment'] = ['Positive','Negative']

# FOR TWEET NUMBER
df_tweet = data.groupby(["time"]).agg({'like':['count','sum'],
                        'reply' : ['sum'],
                        'retweet' : ['sum']
                        }).reset_index()
df_tweet.columns = [col[0] if col[1] == '' else col[0] + '_' + col[1] for col in df_tweet.columns]

# SIDEBAR
# st.sidebar.header("Main")
# val = st.sidebar.selectbox(
#         "Pilih Sentimen",
#         ['Positif', 'Negatif']
#     )
add_logo("https://upload.wikimedia.org/wikipedia/commons/archive/c/ce/20210909091155%21Twitter_Logo.png",150)

# TITLE
"# Analisis Sentimen Media Sosial Peserta Bootcamp BCA 2024"
"Bootcamp Influencer 2024 PT. Benih Citra Asia"

try:
    list_users = df.set_index("fullname")    
    candidate = st.multiselect(
        "Pilih Kandidat", list(list_users.index)
    )
    if candidate:
        data_list = list_users.loc[candidate]
        st.write("### Daftar Kandidat : ", data_list[fullname])
    # else:
        #do nothing
    # if not candidate:
    #     st.error("Silahkan pilih satu kandidat!")
    # else:
    #     data = list_users.loc[candidate]
    #     data = data.rename(columns={'fullname': 'Nama'}, inplace=True)
        
    #     st.write("### Daftar Kandidat : ", data)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
"\n"
a11, a12 = st.columns(2)
a21, a22 = st.columns(2)

# BARIS PERTAMA
with a11:
    st.metric(label="Jumlah Post",
        value=f"{numerize.numerize(data.shape[0])}"
        )
    
    fig = px.line(df_tweet, x='time', y='like_count',
             hover_data=['like_sum', 'reply_sum', 'retweet_sum'], 
             labels={'like_sum':'like',
                     'reply_sum':'reply',
                     'retweet_sum':'retweet',
                     'like_count':'tweet'},
            height=400
            )
    fig.update_yaxes(visible=False, fixedrange=True)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with a12:
    st.metric(label="Jumlah Komentar",
    value=f"{numerize.numerize(data['interaction'].sum().item())}"
    )
    fig = px.line(df_tweet, x='time', y='like_sum',
             hover_data=['like_sum', 'reply_sum', 'retweet_sum'], 
             labels={'like_sum':'like',
                     'reply_sum':'reply',
                     'retweet_sum':'retweet'},
            height=400
            )
    fig.update_yaxes(visible=False, fixedrange=True)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with a21:
    "Wordcloud"
    wc= generate_wordcloud(data['clean'])
    plt.figure(figsize=(10,8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

with a22:
    "Sentimen Pengguna"
    fig = px.pie(df_sentiment, 
            names='sentiment',
            values='total',  
            # title='Sentiment Pengguna',
            hole=.3,
            height=300
            ) 
    fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=18,)
    fig.update_layout(showlegend=False,
                      margin=dict(l=20, r=20, t=20, b=20),
)
    st.plotly_chart(
        fig,
        use_container_width=True
    )
















