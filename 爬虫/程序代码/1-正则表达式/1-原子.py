#正则表达式，原子例子

import re
pat="yue" #普通字符作为原子，三个原子组成一个正则表达式，赋给pat

string="http://yum.iqianyue.com" #string就是要检索的字符串
rst=re.search(pat, string)       #search()是re下面的一个函数
print(rst)

string2="sdfsdfsdfsdfsdg"
rst2=re.search(pat, string2)
print(rst2)

#=====非打印字符作为原子

pat3="\n"
string3= '''sdsfdsfsdfsa
    sdsadsaffg '''   

rst3=re.search(pat3, string3)
print(rst3)

#=====通用字符作为原子
#通用字符：比如'\w'、'\d'、'\s'等

pat="\w\dpython\w" 
                   
string="hjsdfsdgs5python_dgg"
rst=re.search(pat, string)
print(rst)

#===原子表：定义一组平等的原子，通常用中括号[]括起来
pat="pyth[jsz]n" 
             
string="saffregvfpythsnssdd"
rst=re.search(pat, string)
print(rst)




