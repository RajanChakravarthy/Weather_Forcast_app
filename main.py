import streamlit as st
import plotly.express as px
from backend import get_data

# Title and input values for place, date and kind
st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ', value='Paris' )
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select the data to view",
                      ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")

# Plots are plotted only after the place field is entered
if place:
    # Catches the error when the place does not exist
    try:
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            # filtering the temperature and date values
            temperature_value = [data['main']['temp'] for data in filtered_data]
            dates = [data['dt_txt'] for data in filtered_data]
            figure = px.line(x=dates, y=temperature_value, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            sky_condition = [data['weather'][0]['main'] for data in filtered_data]
            dates = [data['dt_txt'] for data in filtered_data]
            # Load images of all weather condition via dictionary
            img_dict = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                        'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            image_paths = [img_dict[condition] for condition in sky_condition]
            st.image(image_paths, width=80, caption=dates)

    except KeyError:
        st.text('The Place does not exists.')
