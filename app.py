from re import I
import string
import streamlit as st
import pandas as pd
st.title("Alphabet To Number") 
data={}
i=1
for letter in string.ascii_uppercase:
    data[letter]=i 
    i+=1
    
a = st.text_input('Enter The Word', 'ABCD')
my_str=[]
my_number=[]
for i in str(a):
    my_str.append(i.upper())
    my_number.append(data[i.upper()])

data = {'alphbate': my_str, 'number': my_number}
df = pd.DataFrame.from_dict(data)
res = any(chr.isdigit() for chr in str(a)
if st.button('Display Number'):
    if res:
        st.write("Enter a string")
    else:
        st.table(df)
