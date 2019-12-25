# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    header= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    # start_urls = ['http://doubn.com/']

    def start_requests(self):
        return [Request("https://accounts.douban.com/login" , callback=self.parse , meta={"cookiejar":1})]

    def parse(self, response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()

        if len(captcha)>0:
            print("此时有验证码")
            localpath = "D:/captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)

            print("请查看本地验证码图片，并输入验证码：")
            captcha_value = input()
            print(captcha_value)
            data = {
                "form_email": "",
                "form_password": "",
                "captcha-solution":captcha_value,  # 验证码的值
                "redir": "",  # 登录后要返回的页面
            }

        else:
            print("此时没有验证码。")
            data = {
                "form_email":"",
                "form_password":"",
                "redir":"",
            }
        print("登录中......")

        return [FormRequest.from_response(response,
                                          meta={"cookiejar":response.meta["cookiejar"]},
                                          headers = self.header ,
                                          formdata=data,
                                          callback=self.next,
                                          )]

    def next(self,response):
        print("此时已经登录成功，并爬取个人中心的数据")

        title = response.xpath("/html/head/title/text()").extract()
        note = response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note)
