#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import sys
import json
# import urllib2

FILENAME = sys.argv[1]
print(sys.argv)
print(FILENAME)

GM_ARR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
BSM_ARR = ["Baisakh", "Jestha", "Asadh", "Shrawan", "Bhadra", "Ashoj",\
        "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

def get_bs_month_num(gmon):
    return BSM_ARR.index(gmon)+1
def get_gmonth_num(smon):
    return GM_ARR.index(smon)+1

# url = "./data/calendar-2079y10m.html"
url = FILENAME
page = open(url)
soup = BeautifulSoup(page.read(), "html.parser")
print(soup[:5])

bs_date = soup.find('h1', {'id': 'yren'}).getText()
gr_date = soup.find('h2', {'id': 'entarikYr'}).getText()

print(bs_date, gr_date)
bsyr = int(bs_date.strip().split(" ")[1])
bsm = bs_date.strip().split(" ")[0] 
gyr = int(gr_date.strip().split(" ")[1])
gm1 = gr_date.strip().split("/")[0]
gm_num = get_gmonth_num(gm1)
bsm_num = get_bs_month_num(bsm)

edate = 0

days = soup.find_all('div', {'class' : 'cells', 'id': 'Cell1'})
# g2bs_dict, bs2g_dict, gs_dict = {}, {}, {}
dic = {}

for d in days:
    dashi = d.find('div', {'id': 'dashi'}).getText().strip()
    gate = d.find('div', {'id': 'nday'}).getText().strip()
    tarik = d.find('div', {'id': 'eday'}).getText().strip()
    fest = d.find('div', {'id': 'fest'}).getText().strip()

    if not gate or not tarik or not dashi:
        continue

    tarikn = int(tarik)
    if tarikn < edate:
        gm_num = (gm_num + 1) % 12
        if gm_num == 1:
            gyr += 1

    g_key = "g{yr}-{mth}-{day}".format(yr=gyr, mth=gm_num, day=tarikn)
    bs_key = "bs{yr}-{mth}-{day}".format(yr=gyr, mth=gm_num, day=gate)

    dic[g_key] = bs_key
    bs_value = {'dashi': dashi, 'fest': fest, 'greg': g_key}
    dic[bs_key] = bs_value

print(dic)

with open("./dict/dict"+FILENAME+".json", 'w') as f:
    f.write(json.dumps(dic))




    # print(dashi, gate, tarik, fest, dashi)



