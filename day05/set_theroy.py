# set: 중복 허용 불가, 집합 개념이라고 보자!!
# a = {1,2,3,1,2,3,1,2,3}
# a.add(4)
# a.discard(3)
# print(a)

# set() - 세트화
b = set([1,2,3,1,2,3,1,2,3])
print(b)

scrip = """
The moves mean, as CNN CEO Mark Thompson said in a note to staffers Monday, that “we will no longer produce morning programming in New York and will be disbanding the team that currently produces CNN This Morning in that city. Our New York-based primetime and weekend programming will continue.” Thompson said CNN would find new roles for Harlow and Mattingly. Mattingly has been told he will have a New York-based role, but people familiar with the matter suggested Harlow and CNN are in ongoing talks. The current morning plans were put into place. quickly. Anchors were said to have been informed of the revamp on Sunday.

Mattingly recently moved his large family to New York for the assignment, and Harlow has served as a steady presence in mornings despite an era of behind-the-scenes chaos at the network under its owner, Warner Bros. Discovery.

The decision appears to bring to an end a years-long effort by CNN to run a New York-based morning program that tried to compete directly with A.M. behemoths like “Today” and “Good Morning America” as well as more direct counterparts like Fox News Channel’s “Fox & Friends” and MSNBC’s “Morning Joe.”
CNN has slogged its way through years of failed A.M. efforts that range from “American Morning” to “Starting Point.” In 2013, former CNN chief Jeff Zucker tried to give the effort a shot in the arm by launching “New Day” with Chris Cuomo, Kate Bolduan and Michaela Pereira. The show, he said at the time, “reminds me of when we put together the ‘Today’ show team in 1996, with Katie and Matt,” a reference to the powerhouse morning-show pair of Katie Couric and Matt Lauer that propelled the NBC program to ratings heights. Under Cuomo and a different co-anchor, Alisyn Camerota, the show gained traction, particularly during Donald Trump’s time in the White House. Later, Berman and Brianna Keilar took the reins of the show."""

# scriplist = scrip.split()
# print(scriplist)
# scripSetList =list(set(scriplist)) # 중복 제거된 리스트
# print(scripSetList)


starbucks ={"아메리카노","라떼","프라프치노","샌드위치", "베이글"}
subway = {"샐러드", "샌드위치", "아메리카노", "랩", "쿠키"}

all_menu = starbucks.union(subway) # 합집합
inter_menu = starbucks.intersection(subway) #교집합
pure_starbucks_menu = starbucks.difference(subway) #차집합
pure_subway_menu = subway.difference(starbucks) #차집합
no_inter_menu = starbucks.symmetric_difference(subway) # 합집합에서 교집합 뺸거
print(no_inter_menu)