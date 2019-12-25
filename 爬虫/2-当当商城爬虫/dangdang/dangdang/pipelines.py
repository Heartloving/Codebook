# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="",user ="", passwd ="", db = "", port=3306)
        cur =conn.cursor()
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]

            sql = "insert into goods(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"

            cur.execute(sql)
            conn.commit()

        conn.close()
        return item
