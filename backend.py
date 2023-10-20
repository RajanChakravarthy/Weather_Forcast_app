import requests

API_KEY = '536bfa48cafc3d78002e6d8767221433'

def get_data(place,days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric'

    # Make requests
    response = requests.get(url)
    content = response.json()
    # Filtering based on dates
    number_of_dates = days * 8
    filtered_data = content['list']
    filtered_data = filtered_data[:number_of_dates]
    return filtered_data


if __name__ == '__main__':
    print(get_data('london', days=2,))
