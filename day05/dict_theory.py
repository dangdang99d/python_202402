# #dict
# # key-vaule, key(고유, only-one)
# # key: int . str
# # vaule: 다됨(하고 싶은거 다됨)
# issac = {
#     'ham': 2500,
#     'cheese': 3000,
#     'bacon': 3000,
# }# 마지막 쉼표 킬포
# print(f"{issac['ham']}") # => 2500
#
# bong = {
#     'eggham': 3800,
#     'soya': 3200,
#     'original': 3000,
# }
#
# cgv = {
#     'popcorn': ['소금', '카라멜','어니언'],
#     'beverage': {
#         'sprite': 2000,
#         'zero_coke': 1500,
#     }
# }
# print(f"{cgv['popcorn'][0]}") # => 소금
# print(f"{cgv['beverage']['zero_coke']}")




mbti={
    'e': '외향적',
    'i': '내향적',
    's': '현실적',
    'n':'미래지향적',
    'f': '감성적',
    't': '발',
    'p': '즉흥적',
    'j': '계획적',
}
your = input("mbti 입력:")
print(f"{mbti[your[0]]},{mbti[your[1]]},{mbti[your[2]]},{mbti[your[3]]}")





