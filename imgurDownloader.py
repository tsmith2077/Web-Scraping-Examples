# Program that will search what you put in 
# and download the images.

import requests, os, bs4

searchedItem = input('What would you like to search for on Imgur?  ')
dirName = 'imgur_' + searchedItem
os.makedirs(dirName, exist_ok=True)
url = 'https://imgur.com//search?q=' + searchedItem
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgElem = soup.select('img')

if imgElem == []:
    print('Image could not be found.')
else:
    print('Downloading images')
    for img in imgElem:
        i = 0
        imgUrl = img['src']
        if 'jpg' in imgUrl or 'jpeg'  in imgUrl:
            if 'https:' not in imgUrl:
                imgUrl = 'https:' + img['src']
            res = requests.get(imgUrl)
            res.raise_for_status()
            imageFile = open(os.path.join(dirName, os.path.basename(imgUrl)), 'wb')
            imageFile.write(res.content)
            imageFile.close()
            i += 1
