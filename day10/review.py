# words =["apple","banana","cherry","date","elderberry","fig"]
# aa =[i for i in words if(len(i)>5 and 'a' in i) ]
# print(aa)
#
# numbers =[30,55,20,75,40,90,10,65]
# bb =[j for j in numbers if j<50 ]
# print(bb)

names =["nami","ahri","jayce","garen","ivern","vex","jinx"]
result =[j for i,j in enumerate(names) if i%5==0]
print(result)

