import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Weather App")

        # Label and Entry for city input
        self.label = tk.Label(root, text="Enter city name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Button to get weather
        self.button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button.pack()

        # Label to display weather info
        self.weather_info_label = tk.Label(root, text="")
        self.weather_info_label.pack()

    def get_weather(self):
        city_name = self.entry.get()
        weather = self.fetch_weather(city_name)
        if weather:
            self.weather_info_label.config(
                text=f"Weather in {city_name}:\n"
                     f"Description: {weather['description']}\n"
                     f"Temperature: {weather['temperature']}°C\n"
                     f"Humidity: {weather['humidity']}%\n"
                     f"Wind Speed: {weather['wind_speed']} m/s"
            )
        else:
            self.weather_info_label.config(text="City not found. Please try again.")

    def fetch_weather(self, city_name):
        # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
        api_key = '95d7f7df7d9327336f42b5a74ec768df'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        response = requests.get(base_url)
        data = response.json()
        if data['cod'] == 200:
            weather_info = {
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
