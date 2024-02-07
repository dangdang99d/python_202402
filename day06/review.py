# movie ={
#
#     '액션 영화': 10000,
#     '로맨틱 코미디': 8000,
#     '공포 영화': 9000,
#     '치즈 팝콘': 6000,
#     '캬라멜 팝콘': 5000,
#     '일반 팝콘': 5000,
# }
#
# print(f"{movie[MOV]}   {movie[pop]}" )

# 쌤풀이
megaMovie = {
    'movie': [
        {'name': '액션 영화', 'price': 10000},
        {'name': '로맨스 코미디', 'price': 8000},
        {'name': '공포 영화', 'price': 9000},
    ]
}
print(f"{megaMovie['movie']}")
number = int(input("영화를 고르세요:(0~2번)"))

print(f"구매하신 영화는 {megaMovie['movie'][number]}")
print(f"구매하신 영화는 {megaMovie['movie'][number]['price']}")
