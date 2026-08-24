import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "7b02d99f0928911c4ebc5d8534b1cddb"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result.config(text="City not found!")
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        output = f"""
City: {city_name}

Temperature: {temp} °C
Humidity: {humidity} %

Weather: {weather}

Wind Speed: {wind} m/s
"""
        result.config(text=output)

    except:
        messagebox.showerror("Error", "Check Internet Connection")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x420")
root.configure(bg="#87CEEB")

title = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), bg="#87CEEB")
title.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

btn = tk.Button(root, text="Get Weather", font=("Arial", 13), bg="green", fg="white", command=get_weather)
btn.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12), bg="#87CEEB", justify="left")
result.pack(pady=20)

root.mainloop()