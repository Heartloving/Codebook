#元组函数的应用
pets=('dog','cat','bird','dog')
print(pets)
for i in range(len(pets)): #遍历元组
    print(pets[i])
print('bird' in pets)
print('cow' in pets)
print(pets.count('dog'))
print(pets.index('dog'))
print(pets.index('mouse'))
