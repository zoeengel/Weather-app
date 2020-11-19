# ZOE ENGEL
# CLASS 1
from tkinter import *
import requests
from tkinter import messagebox

window =Tk()
window.geometry('500x190')
window.title("Weather")
window.config(bg="green")

# WEATHER FUNCTION
def show(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feel = weather['main']['feels_like']

        if showbtn:
            finalstr = 'Place: %s \n' \
                       'Cloud cover: %s \n' \
                       'Temperature: %s \n' \
                       'Feels like: %s'\
            % (name, desc, temp, feel)

    except:
        messagebox.showinfo('ERROR','Enter your city please')

    return finalstr

# GETTING WEATHER INFO
def check(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    weather_key = '3fbdcd505ae2d34b1cdaa3b815767792'
    params = {'appid': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = show(weather)

def exit():
    window.destroy()

# CREATING MY FRAMES AND LABELS
frame = Label(window)
frame.pack(side=TOP)

entlbl = Label(frame, text="Enter city:")
entlbl.pack(side=TOP)
entry = Entry(frame)
entry.pack(side=TOP)

lower_frame = Label(window, bg='white', bd=1)
lower_frame.pack(side=TOP)

label = Label(lower_frame)
label.pack(side=TOP)

# BUTTONS
HEIGHT = 1
WIDTH = 12
showbtn = Button(window, text="Get weather", command=lambda:check(entry.get()),width=WIDTH, height=HEIGHT, bg="white")
showbtn.pack(side=TOP)
exitbtn = Button(window, text="Exit", command=exit,width=WIDTH, height=HEIGHT, bg="white")
exitbtn.pack(side=TOP)

window.mainloop()
