import requests
import json
import datetime
from tkinter import Tk, Label, Entry, Button, LEFT, StringVar, OptionMenu, Frame, Listbox, Scrollbar, END

def get_weather(city):
    api_key = '20f1da27126c74f821b8383c1f93792a'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)

        if data['cod'] != '404':
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            pressure = data['main']['pressure']
            air_pollution = data['main'].get('aqi')

            weather_info = f'WEATHER IN: {city}:\n\nDESCRIPTION: {weather_desc}\nTEMPERATURE: {temperature}°C\nHUMIDITY: {humidity}%\nWIND SPEED: {wind_speed} m/s\nPRESSURE: {pressure} hPa'
            if air_pollution:
                weather_info += f'\nAIR POLLUTION: {air_pollution}'

            return weather_info
        else:
            return 'Unable to find weather data for the specified city.'
    except:
        return 'There was a problem connecting to the weather API.'


def get_forecast(city, days=3):
    api_key = '20f1da27126c74f821b8383c1f93792a'
    base_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)

        if data['cod'] != '404':
            forecast_data = data['list'][:days * 8]

            forecast_info = f'Weather forecast for {city} for the next {days} days:\n\n'

            previous_date = None
            for forecast in forecast_data:
                date = forecast['dt_txt'].split()[0]
                time = datetime.datetime.strptime(forecast['dt_txt'].split()[1], "%H:%M:%S").strftime("%H:%M")
                temperature = forecast['main']['temp']
                weather_desc = forecast['weather'][0]['description']

                if date != previous_date:
                    forecast_info += f'\n\nDate: {date}\n\n'

                forecast_info += f'Time: {time}\n   Temperature: {temperature}°C\n   Description: {weather_desc}\n\n'

                previous_date = date

            return forecast_info
        else:
            return 'Unable to find weather data for the specified city.'
    except:
        return 'There was a problem connecting to the weather API.'


def display_weather():
    city = entry.get()
    weather_info = get_weather(city)
    forecast_listbox.delete(0, END)

    if weather_info.startswith("Unable") or weather_info.startswith("There was a problem"):
        forecast_listbox.insert(END, weather_info)
    else:
        forecast_list = weather_info.split("\n")
        for item in forecast_list:
            forecast_listbox.insert(END, item)


def display_forecast():
    city = entry.get()
    forecast_info = get_forecast(city, int(days_var.get()))
    forecast_listbox.delete(0, END)

    if forecast_info.startswith("Unable") or forecast_info.startswith("There was a problem"):
        forecast_listbox.insert(END, forecast_info)
    else:
        forecast_list = forecast_info.split("\n\n")
        for item in forecast_list:
            forecast_listbox.insert(END, item)

window = Tk()
window.title("PACIOWA POGODYNKA")
window.geometry("450x250")
window.configure(background="#00C5C9")

label = Label(window, text="***   ENTER A CITY   ***", bg="#00C5C9")
label.pack()

entry = Entry(window)
entry.pack()

button_frame = Frame(window, bg="#00C5C9")
button_frame.pack()

weather_button = Button(button_frame, text="Get Weather", command=display_weather)
weather_button.pack(side="left")

forecast_button = Button(button_frame, text="Get Forecast", command=display_forecast)
forecast_button.pack(side="left")

days_var = StringVar(window)
days_var.set("3")
days_dropdown = OptionMenu(button_frame, days_var, "1", "3", "5")
days_dropdown.pack(side="right")

forecast_listbox = Listbox(window, bg="#D0F6E3", width=60)
forecast_listbox.pack()

forecast_scrollbar = Scrollbar(window, orient="vertical")
forecast_scrollbar.pack(side="right", fill="y")

forecast_listbox.config(yscrollcommand=forecast_scrollbar.set)
forecast_scrollbar.config(command=forecast_listbox.yview)

window.mainloop()
