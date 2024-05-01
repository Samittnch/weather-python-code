import requests

def get_weather_report(city_name):
    url = f'https://wttr.in/{city_name}'
    try:
        response = requests.get(url)
        # Print the text from the response
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'City_Name' with the actual city name you want the weather report for
city_name = input("Enter the name of the City: ")
get_weather_report(city_name)
