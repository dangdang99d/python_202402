# #filter(how,what): 걸러주기
# evlist =[2,4,6,8,10]
# res= filter(lambda x:x %4==0, evlist)
# fliterList= list(res)
# print(fliterList)
#
# fruits=['mandarin','kiwi','orange','apple','peach','banana']
# res1 =filter(lambda x:len(x)>=6, fruits)
# f= list(res1)
# print(f)
# resl =filter(lambda x:x[0]=='a' or x[1]=='a' , fruits)
# f= list(resl)
# print(f)

# numbers=[5,10,15,20,25]
# kk=list(map(lambda x: x**2, numbers))
# ree= filter(lambda x:x>=50 and x<=500, kk)
# fliterqq= list(ree)
# print(fliterqq)

words =["hello","world","python","is","crazy"]
ww=filter(lambda x : len(x)>=5,words)
upper=map(lambda x: x.upper(),list(ww))
print(list(upper))


