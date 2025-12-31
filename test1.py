# # 실습1
# money = 300000
# book = 80000
# lunch = 9000
# price = 120000
# plus = 1.2
# elec = 2/3

# money = int(((money - book - 5*lunch + price)*plus)*elec)
# print(f'{money}원')

# # 시작 용돈
# money = 300000

# # 책 구매
# money -= 80000

# # 평일 점심값(9천원씩 5일간)
# money -= 9000*5

# # 과외 알바 수입
# money += 120000

# # 부모님 추가 용돈 (현재 금액의 20%)
# money += money*0.2

# # 전기요금 등으로 1/3 지출
# money -= money/3

# # 최종
# print(f"최종 남은 금액:{int(money)}원")

