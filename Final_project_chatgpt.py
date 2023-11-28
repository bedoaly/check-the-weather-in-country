import requests
import tkinter as tk
from tkinter import messagebox, Label

def get_weather_data(query):
    access_key = '877b27e0f86e50b4c59e706b08abab6b'
    params = {'access_key': access_key, 'query': query}
    response = requests.get('http://api.weatherstack.com/current', params)
    return response.json()

def update_labels(api_response, labels):
    if api_response.get('success', True):
        for key, label in labels.items():
            label.config(text=f'{key.capitalize()} : {api_response["current"][key]}')
    else:
        messagebox.showerror('Error', 'You must enter a valid country')

def search_button_clicked():
    query = txtedit.get(1.0, 'end').strip()
    api_response = get_weather_data(query)
    update_labels(api_response, {
        'temperature': label_vars['temperature'],
        'humidity': label_vars['humidity'],
        'wind_speed': label_vars['wind speed'],
        'pressure': label_vars['pressure'],
        'precip': label_vars['precipitation']
    })

window = tk.Tk()
window.title('Weather Information')
window.minsize(500, 300)

labels = ['Temperature', 'Humidity', 'Wind speed', 'Pressure', 'Precipitation']
label_vars = {label.lower(): Label(window, text=label, font=50) for label in labels}
for i, label_var in enumerate(label_vars.values()):
    label_var.grid(column=0, row=i + 2, padx=10, pady=10)

txtedit = tk.Text(window, height=2, width=20, font=50)
txtedit.grid(column=1, row=0)

frame_button = tk.Frame(window)
frame_button.grid(column=2, row=0, sticky='ns', padx=10, pady=30)

search = tk.Button(frame_button, text='Search', command=search_button_clicked)
search.grid(column=0, row=0, sticky='ns', padx=5, pady=5)

tk.Label(window, text='Location : ', font=50).grid(column=0, row=0, padx=10, pady=10)

window.mainloop()
