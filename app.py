import streamlit as st
import pandas as pd
import duckdb as db

st.write("SQL space repetition system")

option = st.selectbox(
    "What would you like to review ?",
    ("Join", "Groupby", "Window function"),
    index=None,
    placeholder="Select a theme",
)

st.write("You selected :", option)

data={"a":[1,2,3], "b":[4,5,6]}
df=pd.DataFrame(data)

tab1, tab2, tab3=st.tabs(["Onglet1","Onglet2","Onglet3"])

with tab1:
    sql_query=st.text_area(label="entrez votre input")
    result=db.query(sql_query)
    st.write(f"vous avez entrez la query suivante: {sql_query}")
    st.dataframe(result)