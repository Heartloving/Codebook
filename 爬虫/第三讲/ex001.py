#ex001:文件的创建、写入和关闭

def make_story():
    f=open('story.txt','w')
    f.write('Marry had s little lamb,\n')
    f.write('and then she had some more.\n')
    f.close()

make_story()

#在文件末尾添加信息

def add_to_story(line,fname='story.txt'):
    f=open(fname,'a')
    f.write(line)
    f.close()

add_to_story('haha!\n')
