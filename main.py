import pandas as pd
import streamlit as st

df = pd.read_csv("LA_Crime.csv")

st.set_page_config(page_title="StreamLit Example",layout="wide")

with st.container():
  st.write("Crimes that have happened in LA in 2020")
  st.write("---------------------------------------")

st.dataframe(df)
xaxis="ROBBERY"
yaxis=df[df["Crm Cd Desc"] == "Robbery"].shape[0]
st.bar_chart(df,x=xaxis,y=yaxis)
