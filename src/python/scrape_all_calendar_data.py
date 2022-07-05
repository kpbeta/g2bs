import requests
import time

# Total available 1992-2080

for year in range(2064, 2081):
    for month in range(1, 13):
        url = "https://nepalicalendar.rat32.com?selYear={yr}&selMonth={mth}&viewCalander=Show".format(yr=year, mth=month)
        filename = "calendar-{yr}y{mth}m.html".format(yr=year, mth=month)

        req = requests.post(url)
        with open("./data/"+filename, mode="w") as f:
            f.write(req.text)

        time.sleep(2)
        
        print(filename)
    time.sleep(10)

