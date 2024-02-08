import random
#randint(star,end)
print(random.randint(0,10))

#random(): 0과 1 사이의 실수
print(random.random())

#shuffle(): 리스트 섞기
a= [1,2,3,4,5]
random.shuffle(a)
print(a)