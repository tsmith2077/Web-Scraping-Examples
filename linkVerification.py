# Download all links on a webpage and
# determine if the link is good or not.

import requests, os, bs4, re
from urllib.parse import urljoin

url = input('Please enter url link:  ')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
websiteLinks = soup.select('a', href=True)


for link in websiteLinks:
    if 'https:' not in link:
        currentLink = urljoin(url, link)
    try:
        currentLink = link['href']
        res = requests.get(currentLink)
        # 503 blocked by forcing log in. 999 is Linkedin blockers.
        if res.status_code == 200 or res.status_code == 503 or res.status_code == 999:
            print(f'{currentLink} is working fine.')
        else:
            print(f'{currentLink} link is broken.')
            print(res.status_code)
    except:
        continue
