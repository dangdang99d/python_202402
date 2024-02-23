import pandas
import faker
import random
import pokebase as pb

# p = pb.pokemon('pikachu')
# for stat in p.stats:
#     print(f"{stat.stat.name}: {stat.base_stat}")
#
a = ["en_US", "ko_KR", "ja_JP"]
kk=int(input("1번 한국 2번 일본 3번 미국"))
if(kk==1):
    b = []
    for i in range(100):
        fake = faker.Faker("ko_KR")
        b.append(fake.name())
    aa = pandas.Series(b)
    seriesNameList = pandas.Series(aa)
    seriesNameList.to_csv('kor.csv')
elif (kk==2):
    b = []
    for i in range(100):
        fake = faker.Faker("ja_JP")
        b.append(fake.name())
    aa = pandas.Series(b)
    seriesNameList = pandas.Series(aa)
    seriesNameList.to_csv('ja.csv')
elif (kk==3):
    b = []
    for i in range(100):
        fake = faker.Faker("en_US")
        b.append(fake.name())
    aa = pandas.Series(b)
    seriesNameList = pandas.Series(aa)
    seriesNameList.to_csv('eng.csv')



# numList =[i for i in range(10)]
# seriesNumList = pandas.Series(numList)
# print(seriesNumList)
