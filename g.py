import streamlit as st
import plotly.express as px 
from prepare_data import load_data 
from forecast_model import train_prophet

st.set_page_config(layout="wide")
st.title("Supply Chain")

@st.cache_data()

def load_model():
  return load_data()

df=load_model()
store_ids=sorted(df["Store"].unique())
dept_ids=sorted(df["Dept"].unique())

st.sidebar.header("Filter")
selected_store = st.sidebar.selectbox("Select Store", store_ids)
selected_dept = st.sidebar.selectbox("Select Dept", dept_ids)
filtered = df[(df["Store"] == selected_store) & (df["Dept"] == selected_dept)]

fig1=px.line(filtered,x="Date",y="Weekly_Sales",title="sales trend")
st.plotly_chart(fig1,use_container_width=True)

st.subheader("Forecast: Next 90 Days")
forecast_df = train_prophet(selected_store, selected_dept)

fig2=px.line(forecast_df,x="ds",y="yhat",title="Prophet Forecast")
fig2.add_scatter(x=forecast_df["ds"],y=forecast_df["yhat_upper"],mode="lines",name="Upper Bound")
fig2.add_scatter(x=forecast_df["ds"],y=forecast_df["yhat_lower"],mode="lines",name="Lower Bound")
st.plotly_chart(fig2,use_container_width=True)

st.caption("Built with Streamlit by Rishika")

