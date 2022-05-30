import streamlit as st

#計算をする関数
def keisann(a,b,c):
    a,b = int(a),int(b)
    code = {"+":a+b, "-":a-b, "*":a*b, "/":a/b}
    return code[c]

#空白なしの時に数字を符号を分ける関数
def rewrite(value):
    s = value
    int_n = []
    str_n = []
    tmp = []
    code = ["+","-","*","/"]
    n_code = [ i for i in range(10)]
    for S in s:
        z = str(S) in str(n_code)
        x = str(S) in str(code)
        if z == True:
            tmp.append(str(S))
        elif z == False:
            int_n.append("".join(tmp))
            tmp = [] 
            str_n.append(S)
    int_n.append("".join(tmp))
    print(int_n)
    print(str_n)
    return int_n, str_n

#タイトル
st.title('Streamlit 超入門')

#テキストから計算式を受け取る
formula = st.text_input('計算機', "1 + 1 - 3").split()
#計算
if len(formula) == 1:
    num, fu = rewrite(*formula)
else:
    num = [formula[i] for i in range(0,len(formula),2)]
    fu = [formula[i] for i in range(1,len(formula),2)]
tmp = []
tmp.append(num[0])
temporary_substitution = [tmp.append(keisann(tmp[-1],num[i+1],fu[i])) for i in range(len(fu))]

#答えを出力
st.write("答え")
st.write(str(tmp[-1]))
