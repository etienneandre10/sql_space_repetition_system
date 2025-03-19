import streamlit as st
import pandas as pd
import duckdb

st.write("hello world")
data={"a":[1,2,3], "b":[4,5,6]}
df=pd.DataFrame(data)

tab1, tab2, tab3=st.tabs(["Onglet1","Onglet2","Onglet3"])

with tab1:
    sql_query=st.text_area(label="entrez votre input")
    result=duckdb.query(sql_query)
    st.write(f"vous avez entrez la query suivante: {sql_query}")
    st.dataframe(result)