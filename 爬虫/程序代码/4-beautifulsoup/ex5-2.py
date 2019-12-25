import urllib.request
from bs4 import BeautifulSoup

res = urllib.request.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = BeautifulSoup(res,"html.parser")
#book_div = soup.find(attrs={"id":"book"})
book_div = soup.find(attrs={"class":"mod-list book-list"})

book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    print(book.string)
