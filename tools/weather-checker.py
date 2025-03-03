import requests

# API key
api_key = "879b3be170e444eb906104646250303"

# Base URL
base_url = "http://api.weatherapi.com/v1"

def fetch_weather(city_name):
    # Construct the complete API request URL
    complete_url = f"{base_url}/current.json?key={api_key}&q={city_name}"

    # Send an HTTP GET request to the API
    response = requests.get(complete_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response as a Python dictionary
        return response.json()
    else:
        # Return None if there was an error with the request
        return None

def display_weather_info(weather_data):
    if weather_data:
        # Extract relevant data from the API response
        location = weather_data["location"]["name"]  # City name
        region = weather_data["location"]["region"]  # Region/State
        country = weather_data["location"]["country"]  # Country
        temperatureC = weather_data["current"]["temp_c"]  # Temperature in Celsius
        temperatureF = weather_data["current"]["temp_f"]  # Temperature in Fahrenheit
        condition = weather_data["current"]["condition"]["text"]  # Weather condition
        humidity = weather_data["current"]["humidity"]  # Humidity percentage
        wind_speed = weather_data["current"]["wind_kph"]  # Wind speed in kph

        # Print the weather details
        print(f"Weather in {location}, {region}, {country}:")
        print(f"Temperature: {temperatureC}°C / {temperatureF}°F")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} kph")
    else:
        # Print an error message if data could not be retrieved
        print("Error retrieving weather data.")

def main():
    while True:
        print("\nWeather Checker Menu:")
        print("1. Check Weather")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            city_name = input("Enter the city name: ")
            weather_data = fetch_weather(city_name)
            display_weather_info(weather_data)
        elif choice == "2":
            print("Thank you for using the Weather Checker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()