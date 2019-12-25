'''
爬取豆瓣电影页面中主演
'''

from pyquery import PyQuery as pq
print('----爬取豆瓣电影页面中主演----')
doc = pq(url='https://movie.douban.com/subject/26425063/?from=showing')

starrings = doc("a[rel='v:starring']").text()
#print(type(starrings))
#print(starrings)
 
stars = starrings.split()
print('<<%s>>的主演：' % (doc("span[property='v:itemreviewed']").text()))
for star in stars:
     print(star)
