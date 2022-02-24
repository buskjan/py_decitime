# Time calculation library for decimal time

import datetime
import time

time_constant = 100000/86400

def convert_timestamp_deciseconds():
    dt = datetime.datetime.now()
    make_it_seconds = dt.hour*3600 + dt.minute * 60 + dt.second
    decitime=int(make_it_seconds*time_constant)
    deconds = int(round((decitime / 100 - int(decitime / 100)) * 100, 0))
    dinuts = int((decitime / 10000 - int(decitime / 10000)) * 100)
    dours = int((decitime/100000 - int(decitime / 100000)) * 10)
    if dours == 10:
        dours = 0
    time_string = str(dours) + ":" + str(dinuts) + ":" + str(deconds)
    return time_string


while True:
    print(convert_timestamp_deciseconds(), end='\r')
    time.sleep(0.864)
