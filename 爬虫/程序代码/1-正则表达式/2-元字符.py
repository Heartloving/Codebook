#元字符
      
import re
pat=".python..." 
string="dsfsdfpythonjdfdsgf"
rst= re.search(pat,string)
print(rst)

pat = "python|php"  #“或”匹配
string="abdcPHP3432Ppythondfdg"
rst= re.search(pat,string)  #将第一个满足条件的内容输出
print(rst)
