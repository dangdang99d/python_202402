# Tuple
# 읽기 전용, 요소 변경 불가

a = (1,2,3,3,3,3,"🧨")
# len(a) => 4
# a.count(3) => 4
# a.index(2) => 1

venti =("아메리카노", "연유라떼", "바닐라라떼")
newVenti = venti + ("쿠키",) # 더할때 쉼표 킬포
a,b,c,d = newVenti #
print(newVenti)
print(f"{c}") #=> 바닐라 라떼
