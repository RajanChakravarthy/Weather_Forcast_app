import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
day = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select the data to view",
                      ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {day} days in {place}")

dates = ['2023-10-18', '2023-10-19', '2023-10-20']
temperatures = [18, 22, 16]

figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})

st.plotly_chart(figure)