# # 실습5
# memus = {
#     '김밥' : 2500,
#     '삼각김밥' : 1500,
#     '도시락' : 4000
# }
# money = int(input("금액 입력: "))
# memu = input("입력값: ").split(',')
# price = []
# for i in memu:
#     price.append(memus[i])
# if memu:
#     if money >= sum(price):
#         print("구매성공")
#     else:
#         print("금액이 부족")
# else:
#     print("입력한 매뉴가 없음")

# # for문 실습
# # step1
# numbers = [3,6,1,8,4]
# num = []
# for i in numbers:
#     num.append(i*2)
# print(num,"step1")

# # step2
# n = 0
# word = []
# words = ["apple","banana","kiwi","grape"]
# for i in words:
#     n = len(i)
#     word.append(n)
# print(word,"step2")

# # step3
# coordinate = [(1,2),(3,4),(5,6),(7,8)]
# x_values = []
# y_values = []
# for x,y in coordinate:
#     x_values.append(x)
#     y_values.append(y)
# print(x_values,y_values,"step3")