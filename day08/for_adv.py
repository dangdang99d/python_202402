# fruits =["apple", "banana","watermelon","mango","blueberry"]
#
# #enumerate(): 번쨰, 요소 출력
# for i in fruits:
#     print(i)
# for i,j in enumerate(fruits):
#     print(f"{i}번째 {j}")

# fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]
#
#
# for i, j in enumerate(fruits):
#     if j.count('a')==0:
#         print(i)



## 리스트 컴프리헨션
a =[i*i for i in range(11)]
print(a)
b =[i+10 for i in range(11)]
print(b)

fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]
fruits =[i.upper() for i in fruits]
print(fruits)