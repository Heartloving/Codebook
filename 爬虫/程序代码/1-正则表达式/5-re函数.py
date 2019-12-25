#正则表达式的函数
#re.match()函数：必须从头开始匹配
#re.search()函数：从一字符串中搜索出一个满足条件的模式
#re.sub()函数：用于替换

import re

pat="p.*y"
string="abcddjfpythonsdfsdfpydff"
rst=re.search(pat,string)  #前面的例子
print(rst)

rst=re.match(pat,string)  #采用match匹配，会看第一个字母是不是p
print(rst)

#修改string
string="phsdfsdfssgfbasdyvfgu"
rst=re.match(pat,string)  
print(rst)

#search还有一个缺点：只能出现一个结果
pat="p.*?y"
string="asfavgtpfdffynjbcajsfpvddftycc"
rst=re.search(pat,string)  
print(rst)

#全局匹配函数
rst=re.compile(pat).findall(string)
print(rst)






