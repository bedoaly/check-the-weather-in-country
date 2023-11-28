import requests
from tkinter import messagebox, Label
import tkinter as tk


def Search(s, label_temp, label_Humid, label_windspeed, label_pressure, label_preci):
    params = {
        'access_key': '877b27e0f86e50b4c59e706b08abab6b',
        'query': s
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    api_response1 = api_result.content
    print(api_response1)
    if api_result.status_code == 200 and api_response.get('success', True):
        label_temp.config(text='Temperature : ' + str(api_response['current']['temperature']) + '°C')
        label_Humid.config(text='Humidity : ' + str(api_response['current']['humidity']) + '%')
        label_windspeed.config(text='Wind speed : ' + str(api_response['current']['wind_speed']) + 'km/h')
        label_pressure.config(text='Pressure : ' + str(api_response['current']['pressure']) + 'hPa')
        label_preci.config(text='Precipitation : ' + str(api_response['current']['precip']) + '%')
    else:
        messagebox.showerror('Error ', 'You must enter a valid country')


window = tk.Tk()
window.title('Abdallah Aly texteditor')
window.minsize(500, 300)
txtedit = tk.Text(window, height=2, width=20, font=50)
frame_button = tk.Frame(window)
label_temp = Label(window, text='Temperature', font=50)
label_temp.grid(column=0, row=2, padx=10, pady=10)
label_Humid = tk.Label(window, text='Humidity', font=50)
label_Humid.grid(column=0, row=3, padx=10, pady=10)
label_windspeed = tk.Label(window, text='Wind speed', font=50)
label_windspeed.grid(column=0, row=4, padx=10, pady=10)
label_pressure = tk.Label(window, text='Pressure', font=50)
label_pressure.grid(column=0, row=5, padx=10, pady=10)
label_preci = tk.Label(window, text='Precipitation', font=50)
label_preci.grid(column=0, row=6, padx=10, pady=10)
txtedit.grid(column=1, row=0)
search = tk.Button(frame_button, text='Search',
                   command=lambda: Search(txtedit.get(1.0, 'end'), label_temp, label_Humid, label_windspeed,
                                          label_pressure, label_preci))
frame_button.grid(column=2, row=0, sticky='ns', padx=10, pady=30)
search.grid(column=0, row=0, sticky='ns', padx=5, pady=5)
tk.Label(window, text='Location : ', font=50).grid(column=0, row=0, padx=10, pady=10)

window.mainloop()
