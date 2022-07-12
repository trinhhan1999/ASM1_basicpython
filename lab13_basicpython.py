from bs4 import BeautifulSoup
import requests as req

resp = req.get('http://py4e-data.dr-chuck.net/comments_1430669.html')

soup = BeautifulSoup(resp.text, 'lxml')
cmt = 0 
for tag in soup.find_all('span'):
    print(tag.text)
    cmt += int(tag.text)
print(cmt)
