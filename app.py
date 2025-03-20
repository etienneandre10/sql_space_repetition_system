import io

import streamlit as st
import pandas as pd
import duckdb as db

st.write("SQL space repetition system")


csv='''
beverage, price
orange juice, 2.5
expresso, 2
tea, 2
'''

beverages=pd.read_csv(io.StringIO(csv))

csv2='''
food, price
chocolatine,1
croissant,2
gateau,3
'''

food=pd.read_csv(io.StringIO(csv2))

answer='''
SELECT * FROM beverages
CROSS JOIN food
'''

solution=db.sql(answer)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ("Join", "Groupby", "Window function"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected :", option)

st.header('enter your code:')
query=st.text_area(label="votre code sql ici", key="user input")

if query:
    result=db.sql(query)
    st.dataframe(result)

    if len(result.columns)!=len(solution.columns)
    ): #replace with try result = result[solution.columns]
    st.write("Some columns are missing")

    n_lines_differences=result.shape[0] - solution.shape[0]
    if n_lines_differences !=0:
        st.write(
            f"result has a {n_lines_differences} lines difference with the solution"
        )
tab2, tab3=st.tabs(["Tables","Solutions"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food")
    st.dataframe(food)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)