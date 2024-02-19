
a=lambda x,y:  x+y
b=lambda x,y:  x+y
c=lambda x,y:  x+y

#map(how,what):
rank=['이병','일병','상병','병장']
def rankToSalary(rank):
    salary={
        '이병': 60,
        '일병':68,
        '상병':80,
        '병장':100

    }
    return salary[rank]

a=map(rankToSalary,rank)
print(list(a))


