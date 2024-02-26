def solution1(my_str,n):
    result=[]
    for i in range(0,len(my_str),n):
        result.append(my_str[i:i+n])
    return result

print(solution1("asdfasdfasdfasd",6))
def solution2(s):
    words=s.split(" ")
    jadenCaseWords =[]
    for i in words:
        if i:
            jadenCaseWords =i[0].upper() + i[1:].islower()
        else:
            jadenCaseWords =i
        jadenCaseWords.append(jadenCaseWords)
    return " ".join(jadenCaseWords)

import pandas
import faker
fake = faker.Faker('ko_KR')
korName =[fake.name() for i in range(100)]
seriesName = pandas.Series(korName)
print(seriesName)