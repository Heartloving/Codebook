#ex002.py:使用readline()读文件
f=open("story.txt")
while True:
    line = f.readline()
    if line:
        print(line)
    else:
        break
f.close
