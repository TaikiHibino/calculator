import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import re

#計算をする関数
def keisann(a,b,c):
    a,b = int(a),int(b)
    code = {"+":a+b, "-":a-b, "*":a*b, "/":a/b}
    return code[c]

#タイトル
st.title('Streamlit 超入門')

#テキストから計算式を受け取る
formula = st.text_input('計算機', "1 + 1 - 3").split()
#計算
num = [formula[i] for i in range(0,len(formula),2)]
fu = [formula[i] for i in range(1,len(formula),2)]
tmp = []
tmp.append(num[0])
temporary_substitution = [tmp.append(keisann(tmp[-1],num[i+1],fu[i])) for i in range(len(fu))]

#答えを出力
st.write("答え")
st.write(str(tmp[-1]))
st.markdown(tmp[-1])
