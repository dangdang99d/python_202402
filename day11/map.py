def abc(a):
    a()
    print('hello')
def hi():
    print('hi')
abc(hi)

a=[2,3,4,5,6]
res = map(lambda x : x*2,a)
print(list(res)) # list화 하는것이 중요하다.


import random

eggs =["" for i in range(0,100)]
def hatchEggs(x):
    cc= ['계란' if i<=30 else j for i,j in enumerate(x)]
    random.shuffle(cc)
    return cc

