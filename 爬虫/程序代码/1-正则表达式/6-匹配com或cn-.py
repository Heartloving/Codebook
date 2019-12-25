#匹配.com或.cn网址

import re

pat = "[a-zA-Z]+://[^\s]*[.com|.cn]"
    
string='<a href="http://www.ucas.ac.cn">中国科学院大学</a>'
rst= re.compile(pat).findall(string)
print(rst)
