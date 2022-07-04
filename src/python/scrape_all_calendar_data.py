import requests
import time

for year in range(1992, 2081):
    for month in range(1, 13):
        url = "https://nepalicalendar.rat32.com?selYear={yr}&selMonth={mth}&viewCalander=Show".format(yr=year, mth=month)
        filename = "calendar-{yr}y{mth}m.html".format(yr=year, mth=month)

        req = requests.post(url)
        with open("./data/"+filename, mode="w") as f:
            f.write(req.text)

        time.sleep(2)
        
        print(filename)
    time.sleep(10)

