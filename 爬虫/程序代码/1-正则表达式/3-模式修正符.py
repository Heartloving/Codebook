#模式修正符
#正常情况下，正则表达式是区分大小写的
#大写字母‘I’：不区分大写

import re
pat="python"
string='''sdfsghdgfPythondgffg
ggdsdspythonffkjj'''
rst=re.search(pat,string) #大小写，所以没有匹配成功
print(rst)

rst=re.search(pat,string,re.I)
print(rst)

