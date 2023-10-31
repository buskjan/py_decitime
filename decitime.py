#!/usr/bin/python3
# Time calculation library for decimal time

import datetime
import time
import tkinter
from tkinter import ttk

time_constant = 100000/86400


def convert_timestamp_deciseconds():
    dt = datetime.datetime.now()
    make_it_seconds = dt.hour*3600 + dt.minute * 60 + dt.second
    decitime = int(make_it_seconds * time_constant)
    deconds = int(round((decitime / 100 - int(decitime / 100)) * 100, 0))
    # deconds = int((decitime / 100 - int(decitime / 100)) * 100)
    dinuts = int((decitime / 10000 - int(decitime / 10000)) * 100)
    dours = int((decitime / 100000 - int(decitime / 100000)) * 10)
    if dours == 10:
        dours = 0
    #time_string = "\033[1;35m" + set_leading_zero(str(dours)) + ":" + \
    time_string = set_leading_zero(str(dours)) + ":" + \
                                set_leading_zero(str(dinuts)) + ":" + \
        set_leading_zero(str(deconds))
    klocka_string.set(time_string)
    klocka.after(400, convert_timestamp_deciseconds)
    #return time_string


def set_leading_zero(string):
    string = string.zfill(2)
    return string

# window
window = tkinter.Tk()
window.title('Decimal tid')
window.geometry('300x150')
klocka_string = tkinter.StringVar()
klocka = ttk.Label(
        master = window, 
        font=("Helvetica", 22), 
        textvariable = klocka_string)
klocka.pack()

convert_timestamp_deciseconds()
# run
window.mainloop()

#while True:
#    print(convert_timestamp_deciseconds(), end='\r')
#    time.sleep(0.864)
    # time.sleep(0.108)
