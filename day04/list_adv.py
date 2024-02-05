menu = ["커피","빵","쥬스"]
menu.append("샌드위치")
menu.remove("쥬스")
menu.sort() #정렬
menu.reverse()
numList = [1,2,3,4,5]
numList.reverse() # 역 정렬
print(numList)
print(menu)
news ="""CNN is facing a backlash from its own staff over editorial policies they say have led to a regurgitation of Israeli propaganda and the censoring of Palestinians perspectives in the network’s coverage of the war in Gaza.

Journalists in CNN newsrooms in the US and overseas say broadcasts have been skewed by management edicts and a story-approval process that has resulted in highly partial coverage of the Hamas massacre on 7 October and Israel’s retaliatory attack on Gaza.

“The majority of news since the war began, regardless of how accurate the initial reporting, has been skewed by a systemic and institutional bias within the network toward Israel,” said one CNN staffer. “Ultimately, CNN’s coverage of the Israel-Gaza war amounts to journalistic malpractice.”

According to accounts from six CNN staffers in multiple newsrooms, and more than a dozen internal memos and emails obtained by the Guardian, daily news decisions are shaped by a flow of directives from the CNN headquarters in Atlanta that have set strict guidelines on coverage.

They include tight restrictions on quoting Hamas and reporting other Palestinian perspectives while Israel government statements are taken at face value. In addition, every story on the conflict must be cleared by the Jerusalem bureau before broadcast or publication."""

news1 = news.split(" ")
news1.sort()
print(news1)