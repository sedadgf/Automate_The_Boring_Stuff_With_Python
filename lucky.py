#This program searches products on Amazon website, than opens at most 5 products
#on new tabs

import requests, sys, webbrowser, bs4

if len(sys.argv)>1:
    product=' '.join(sys.argv[1:])
else:
    print('Type to search...')
    product=input()

url='https://amazon.co.uk/s?k=' + product
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 \
            Safari/537.36'}
res = requests.get(url, headers=headers)
print('Shopping...')
res.raise_for_status()

#Retrieve top search results links.
soup=bs4.BeautifulSoup(res.content, 'lxml')

#open a browser tab for each result
linkElems=soup.find_all('a', class_='a-link-normal a-text-normal')
numOpen=min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.amazon.co.uk' + linkElems[i].get('href'))
