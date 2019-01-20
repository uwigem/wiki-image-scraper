from imagesTodo import images, baseLink, imageLinkPrefix
from bs4 import BeautifulSoup as bs
import requests as r

finalUrls = []

for image in images:
    specialLink = baseLink + imageLinkPrefix + image
    imageAllHTML = r.get(specialLink)
    imageParsedHTML = bs(imageAllHTML.content, 'html.parser')
    link = imageParsedHTML.select('td.filehistory-selected')[0].a.get('href')
    fullLink = baseLink + link
    finalUrls.append(fullLink)

[print(url) for url in finalUrls]
