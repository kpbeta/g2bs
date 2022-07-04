#!/usr/bin/env python3
import requests
import bs4

page = requests.get("https://nepalicalendar.rat32.com")
# print(page.content)

soup = bs4.BeautifulSoup(page.content, "html.parser")
today_div = soup.find_all('div', id='Cell1', attrs = {"style": "text-decoration:blink;background:radial-gradient(ellipse at center center , white 0%, #33CCFF 100%) repeat scroll 0 0 rgba(0, 0, 0, 0) !important"})
month_div = soup.find('div', id='mth')
year_div = soup.find('div', id='yr')

for d in today_div:
    tarik = d.find("div", id="nday").get_text().strip()
    tithi = d.find("div", id="dashi").get_text().strip()
    chaad = d.find("div", id="fest").get_text().strip()
mahina = month_div.get_text().strip()
barsa = year_div.get_text().strip().split(" ")[0].strip()

# print(today_div)
# print(month_div)
# print(year_div)

print("%s %s, %s (%s) %s" % (str(mahina), str(tarik),
                                str(barsa), str(tithi), str(chaad))) 
