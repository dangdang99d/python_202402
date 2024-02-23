import pandas
import faker
import random
import pokebase as pb

# p = pb.pokemon('pikachu')
# for stat in p.stats:
#     print(f"{stat.stat.name}: {stat.base_stat}")
#

b=[]
for i in range(100):
    a = ["en_US", "ko_KR", "ja_JP"]
    fake= faker.Faker(random.choice(a))
    b.append(fake.name())
aa=pandas.Series(b)
print(aa)
seriesNameList = pandas.Series(aa)
seriesNameList.to_scv('./mega.csv')

# numList =[i for i in range(10)]
# seriesNumList = pandas.Series(numList)
# print(seriesNumList)
