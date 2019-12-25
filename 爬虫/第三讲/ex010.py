#ex010.py:pickle二进制文件存取
import pickle

def make_picked_file():
    grades={'tom':[84,88,90,90],
            'jack':[77,87,97,88],
            'marry':[85,None,90,90],
            'alan':[100,88,90,95]}
    outfile=open('grades.dat','wb')
    pickle.dump(grades,outfile)

def get_pickle_data():
    infile=open('grades.dat','rb')
    grades=pickle.load(infile)
    return grades

make_picked_file()
print(get_pickle_data())
