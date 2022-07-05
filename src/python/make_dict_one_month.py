from bs4 import BeautifulSoup
import re
# import urllib2

url = "./data/calendar-1992y4m.html"
page = open(url)
soup = BeautifulSoup(page.read(), "html.parser")

# cities = soup.find_all('span', {'class' : 'city-sh'})

# for city in cities:
#         print city


days = soup.find_all('div', {'class' : 'cells', 'id': 'Cell1'})
bs_date = soup.find('h1', {'id': 'yren'}).getText()
gr_date = soup.find('h2', {'id': 'entarikYr'}).getText()


print(bs_date, gr_date)
gyr = gr_date.strip().split(" ")[1]
gm1 = gr_date.strip().split("/")[0]
print(gm1,gyr)


# dic = 

# for day in days:
#         print(date)
# # print(soup)
