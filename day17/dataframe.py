# dataframe
import pandas
import faker
import random
# data ={
#
#     'name':['기민서','권성혁','김태양','안지우'],
#     'age':[25,15,15,21],
#     'city':['과천시','서울시','서울시','도쿄']
#
# }
# dataFramedData=pandas.DataFrame(data)
# print(dataFramedData)
# cof=['아아','라떼','모카','바닐라','디카페인']
#
# fake = faker.Faker("ko_KR")
# nameList =[fake.name() for i in range(1000)]
# ageList=[random.randint(20,50) for i in range(1000)]
# coffeeList = [random.choice(cof) for i in range(1000)]
#
#
# data ={
#     '손놈': nameList,
#     '나잇대': ageList,
#     '커피 판매 이름': coffeeList
# }
# dataFrameCoffee = pandas.DataFrame(data)
# dataFrameCoffee.to_csv('맥아커피.csv')

# data ={
#     'name':b,
#     'age':[25,15,15,21],
#     'city':['과천시','서울시','서울시','도쿄']=
#
# }// 20~50
# dataFramedData=pandas.DataFrame(data)
# print(dataFramedData)

def makeName():
    c = ["en_US", "ko_KR", "ja_JP"]
    fake = faker.Faker(random.choice(c))
    return fake.name()
plane_weight=[100,0,0,0,0,0]
name=[makeName() for i in range(1000)]
age =[random.randint(10,70) for i in range(1000)]
plane =[random.choices(['제주항공','에어서울','티웨이','진에어','대한항공','아시아나'],weights=plane_weight,k=1) for i in range(1000)]
tour= [random.choice(['맛집탐방','온천여행','야구관광','맥주투어','힐링']) for i in range(1000)]
city=[random.choice(['후쿠오카','벳푸','오이타','나가사키','가고시마']) for i in range(1000)]
data={
    '이름':name,
    '나이':age,
    '항공':plane,
    '투어':tour,
    '도시':city
}
dataFramePlane =pandas.DataFrame(data)
dataFramePlane.to_csv('여행 리스트.csv')
