import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time # 時間を扱う機能をインポート

#ヘッダー表示
st.header("streamlitテストアプリ")
#タイトル表示
st.title("Webアプリ開発中")
#テキスト表示
st.write("生活用アプリ")

#スライダー（デフォルトでは0~100）
st.title("スライダー")
weight = st.slider("今日の体重は")
st.write("今の体重は" + str(weight) +"kgです")

# pip install streamlit pandas
df = pd.DataFrame(
    {'人数': [10, 20, 30],
    'バスの手配': [False, True, True]},
    index=['名古屋店', '大阪店', '新宿店']
)
edited_df = st.data_editor(df)

# レイアウトとして２列を定義
col1, col2 = st.columns(2)

# 1列目をwithで囲む
with col1:
    st.write("列1がここに表示されます")

# 2列目をwithで囲む
with col2:
    st.write("列2がここに表示されます")



st.sidebar.write("hello world") #.sidebar付けるとサイトバーに出力されます。



import numpy as np # 数列を扱う機能をインポート
import pandas as pd # データフレームを扱う機能をインポート

# 乱数の配列を作るメソッドを作ります。引数r,cとし、それぞれおのデフォルト値を10と5に設定します。
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))# 乱数10の５個の数列を作ります。カラムの設定は0-4の名前を付けます。
    return df # 作ったデータフレームを返します。

dataframe = rand_df(r=10,c=3) # rに10、cに3を代入したrand_dfメソッドを処理します。

# 表の描画します。
st.dataframe(dataframe.head(n=3))
# データフレームのチャートの描画します。
st.line_chart(dataframe)