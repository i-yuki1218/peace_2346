# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:10:26 2021

@author: yuki
"""
import streamlit as st

st.title('～心理テスト～')
st.write('こんにちはpeaceです！ここでは、簡単な心理テストが受けられます。')
st.write('結果は絶対に当たるとは限りません。参考までに取り組むことをお勧めします！')

text=st.text_input('あなたのニックネームを入力してください')
'あなたは, ',text,'です'

old=st.slider('あなたの年齢を入力してください？',0,100,20)
'年齢',old

birthday=st.selectbox('Birthday'['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月',])
