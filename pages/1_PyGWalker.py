import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc # streamlit 機能を拡張
import openpyxl
import pygwalker as pyg
import json

# pip install pandas streamlit openpyxl pygwalker

st.set_page_config(page_title='PyGWalker', layout='wide')
st.title('PyGWalker')

#encoding設定
selected_encoding = st.selectbox(
    'encodingを選択', 
    ['utf-8', 'shift_jis', 'cp932'],
    key='encoding')


# CSVとJSONファイルの両方を受け入れるように変更
uploaded_file = st.file_uploader('ファイルをアップロード', type=['csv', 'json'])

if uploaded_file:
    # ファイルの拡張子によって処理を分岐
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file, encoding=selected_encoding)
    elif uploaded_file.name.endswith('.json'):
        # JSONファイルを文字列として読み込む
        json_str = uploaded_file.getvalue().decode(selected_encoding)
        data = json.loads(json_str)
        # "@graph"キーのデータをデータフレームに変換
        df = pd.DataFrame(data['@graph'])
    else:
        st.error('サポートされていないファイル形式です。')
        st.stop()
    
    # # PyGWalkerを使用してHTMLに変換 return_html=Trueとすることで、HTML形式の文字列
    # pyg_html = pyg.walk(df, return_html=True)
    pyg_obj = pyg.walk(df)
    pyg_html = pyg_obj.to_html()
    ## 生成したHTMLをStreamlitアプリケーションに埋め込む
    stc.html(pyg_html, scrolling=True, height=1000) #CSS pixels
