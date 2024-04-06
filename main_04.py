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

#ボタン
st.title("今日の天気は")
st.button("リセット", type="primary")
if st.button("晴れ？"):
    st.write("今日も元気に！")
else:
    st.write("傘を忘れずに!")

#テキスト入力
st.title("やること")
st.text_input("今やること", key="do")
st.session_state.do #keyでアクセス

#チェックボックス
st.title("ごみ捨てチェック")
is_agree = st.checkbox("ごみ捨てた？")
if is_agree:
    st.write("お疲れ様！")
else:
    st.write("忘れずに！")

# レイアウトとして２列を定義
col1, col2 = st.columns(2)

# 1列目をwithで囲む
with col1:
    st.write("列1がここに表示されます")

# 2列目をwithで囲む
with col2:
    st.write("列2がここに表示されます")



st.sidebar.write("hello world") #.sidebar付けるとサイトバーに出力されます。
st.text_input("ここに文字が入力できます。") # テキストを入力できます。


# 選択肢を配列で指定して選択肢を出力します。
st.selectbox("選んでください。",["選択肢1","選択肢2","選択肢3"])



# ダウンロードする文字を定義し、output_textに代入します。
output_text = "この文字がダウンロードされます"

# 代入された文字をダウンロードするボタンを設置。オプションは内容をdataに指定、ファイル名をfile_nameに指定、ファイルタイプをmimeに指定
st.download_button(label='記事内容 Download', 
                data=output_text, 
                file_name='out_put.txt',
                mime='text/plain',
                )



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