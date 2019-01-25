import sys
import json
import requests
import re
from bs4 import BeautifulSoup
frm = int(sys.argv[1])
to = int(sys.argv[2])
url = "https://summerofcode.withgoogle.com/archive/{year}/projects/?page={page}"
orgs = {}
for year in range(frm,to+1):
    page_num = 1
    while True:
        r = requests.get(url.format(year=year,page=page_num))
        print("year=",year,"page=",page_num)
        if r.status_code == 404 :
            break
        page_num+=1
        soup = BeautifulSoup(r.content, 'html5lib')
        headings = soup.find_all('div', attrs = {'class':'archive-project-card__header'})
        for heading in headings:
            #student_name = heading.find("h4").find("a").text
            org_name = str(heading.find(text=re.compile("^Organization:"))).split(":")[1].strip().lower()
            if not orgs.get(year):
                orgs[year] = {}
            orgs[year][org_name] = orgs[year].get(org_name,0) + 1
with open('data.json', 'w') as fp:
    json.dump(orgs, fp)

# plot(orgs)

