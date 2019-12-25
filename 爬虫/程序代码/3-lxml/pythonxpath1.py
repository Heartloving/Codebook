from lxml import etree
 
html_str = """
<div id="box1">this from blog.csdn.net/lncxydjq , DO NOT COPY!
    <div id="box2">*****
        <!--can u get me, bitch?-->
    </div>
</div>
"""
 
html = etree.HTML(html_str)
 
print(html.xpath('//div[@id="box1"]/div/node()')[1])
print(type(html.xpath('//div[@id="box1"]/div/node()')[1]))
print(html.xpath('//div[@id="box1"]/div/node()')[1].text)

