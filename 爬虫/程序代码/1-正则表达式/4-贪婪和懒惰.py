#贪婪和懒惰模式
import re
pat1="p.*y" 

string="abcddjfpythonsdfsdfpydff"
rst=re.search(pat1,string)
print(rst)

pat2="p.*?y" #这是一种懒惰模式
rst=re.search(pat2,string)
print(rst)

