#!/usr/bin/env python3

import requests
import time

# Total available 1992-2080

for year in range(1992, 2081):
    for month in range(1, 13):

        url = "https://nepalicalendar.rat32.com/"
        payload = "selYear={yr}&selMonth={mth}&viewCalander=Show".format(
                yr=year, mth=month)
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        filename = "calendar-{yr}y{mth}m.html".format(yr=year, mth=month)
        with open("./data/"+filename, mode="w") as f:
            f.write(response.text)

        time.sleep(2)
        print(filename)
    
    time.sleep(10)

