import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import random
import datetime

# 今回のデータ生成に使う関数
def distance(x, y):
# 東京タワーの座標を基準に値を生成する
    _x = 139.745433
    _y = 35.658581
    return ((x - _x)**2 + (y - _y)**2)**0.5

# ランダムなデータをnum_rows行を生成する
num_rows = 3000
df = pd.DataFrame(index=range(num_rows), columns=['名称', '緯度', '経度'])
df['名称'] = [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7)) for i in range(num_rows)]
df['緯度'] = [random.uniform(34, 38) for i in range(num_rows)]
df['経度'] = [random.uniform(135, 141) for i in range(num_rows)]
df['距離'] = [distance(df['経度'][i], df['緯度'][i]) for i in range(num_rows)]
df['カテゴリ'] = [random.randint(1, 10) for i in range(num_rows)]
df['バリュー'] = [random.random() * 100 for i in range(num_rows)]

# Streamlitページの幅を調整する
st.set_page_config(layout="wide")

# Pygwalkerを使用してHTMLを生成する
# pyg_html = pyg.walk(df, env='Streamlit', return_html=True, dark='light')
pyg_obj = pyg.walk(df)
pyg_html = pyg_obj.to_html()

# HTMLをStreamlitアプリケーションに埋め込む
components.html(pyg_html, width=1300, height=1000, scrolling=True)
