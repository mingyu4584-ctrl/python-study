# # 조건문
# # and 둘 다 True일 때만 True
# a = 10
# b = 5

# print(a > 5 and b > 3)  # True
# print(a > 5 and b > 10) # False
# # 하나라도 False면 결과는 False

# # or 둘 중 하나라도 True면 True
# print(a > 5 or b > 10)  # True
# print(a < 5 or b > 10)  # False

# # not True <-> False 뒤집기
# print(not a > 5)    # False
# print(not a < 5)    # True

# age = 10
# if age >= 18:
#     print("성인 입니다.")   # 해당 값이 True면 실행
# else:
#     print("미성년자 입니다.")   # 해당 값이 False면 실행
# # 삼항 연산자
# print("성인 입니다." if age >= 18 else "미성년자 입니다.")

# score = 82

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# # 예시 놀이이구 탑승 가능 여부
# # 조건 : 키가 140cm 이상 그리고 나이가 10살 이상이면 탑승 가능

# height = int(input("키 입력: "))
# age = int(input("나이 입력: "))

# if height >= 140 and age >= 10:
#     print("탑승 가능")
# else:
#     print("탑승 불가")
    
# num = int(input("숫자 입력: "))

# if num%2==0:
#     print("짝수")
# else:
#     print("홀수")

# name = input("이름을 입력")

# if name == 'Jon':
#     print("당신은 Jon 이야!")
# else:
#     print("당신 누구야?")

# # 예시 : 시험 응시 가능 여부
# # 조건 : 나이 20세 이상, 출석률 80% 이상, 미납 요금 없음

# age = 22    # 나이
# attendace = 85  # 출석률
# fee_paid = True # 미납 현황
# scholarship = False  # 장학금 대상 여부

# if age >= 20 and attendace >= 80 and (fee_paid or scholarship):
#     print("시험 응시 가능")
# else:
#     print("시험 응시 불가")

# # 중첩 if 문
# is_login = True # 로그인 여부
# age = 17    # 나이

# if is_login:
#     print("로그인 성공")
#     if age >= 19:
#         print("환영합니다!")
#     else:
#         print("미성년자는 이용 할 수 없습니다.")
#         is_login = False
#         if is_login == False:
#             print("로그아웃 되었습니다.")
#         else:
#             print("로그아웃에 실패 하였습니다.")
# else:
#     print("로그인이 필요 합니다.")

# is_member = input("회원인가요? (y/n): ")
# age = int(input("나이를 입력하세요: "))
# with_parent = input("보호자 동반인가요? (y/n): ")
# is_night = input("야간 상영인가요? (y/n): ")
# if is_member=='y' and age >= 19:
#     print("입장 가능")
#     if with_parent=='y'and is_night=='n':
#         print("입장 가능")
# else:
#     print("입장 불가능")

# # range(5) -> 0 <= 숫자 < 5
# for i in range(3, 6):
#     print(i)

# nums = [1,2,3,4,5]

# total = 0

# # nums에서 하나씩 꺼내서 total에 누적
# for n in nums:
#     total += n  # total = total + n
# print(total)

# coords = [(1,2),(3,4),(5,6)]
# for y,x in coords:
#     print(f"x:{x}, y:{y}")

# person = {'name':"alice","age":30}

# for key,value in person.items():
#     print(f"키값: {key}, 벨류값: {value}")

# numbers = {3,1,4,1,5}

# for num in numbers:
#     print(num)

# # 예시
# for i in range(2,31):
#     for j in range(1,31):
#         print(f"{i}x{j}={i*j}")

# # 예시
# nums = [[[1,2]],[[3,4]],[[5,6]]]

# for a in nums:
#     for b in a:
#         for n in b:
#             print(n)

# for i in range(10):
#     if i == 5:    # i가 5가 되면 즉시 종료
#         break
#     print(i)

# nums = [1,2,3,4,5,6,7,8]

# for n in nums:
#     if n == 5:
#         break
#     print(n)

# # continue 이번 반복만 건너뛰고, 다음 반복으로 넘어감(반복문은 끝나지 않아요!)
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# # pass 아무 동작도 하지 않고 자리만 차지
# for i in range(3):
#     pass    # 추후 구현 예정인 자리
# # 프로그램에 영향 없음
# # 반복문 실행 블록 구현 전 에러 방지용으로 사용됨

# # for - else -> for문이 break 없이 끝났을 때만 else 실행
# # if의 else 아님
# # break가 있었는지가 핵심
# for i in range(3):
#     if i == 1:
#         break
#     print(i)
# else:
#     print("끝 !")

# # 일반 for문에서
# nums = []
# for i in range(5):
#     nums.append(i)

# num = [i*2 for i in range(5)]
#     # [넣을 값 for 변수 in 반복대상]

# number = [i for i in range(10) if i % 2 == 1]

# squares = {x: x**2 for x in range(1,6)}

# i = 0

# while 1<5:
#     print(i)
#     i +=1
#     if(i > 100):
#         break

# while True:
#     text = input("end면 종료: ")

#     if text == "end":
#         print("종료 되었습니다.")
#         break
#     print("입력",text)

# i = 1

# while i <= 100:
#     if i % 2 ==0:
#         print(i)
#     i+=1

# # map 예시

# users = [
#     {"name":"철수1","age":1},
#     {"name":"철수2","age":56},
#     {"name":"철수3","age":81},
#     {"name":"철수4","age":24},
#     {"name":"철수5","age":13},
#     {"name":"철수6","age":5},
#     {"name":"철수7","age":55},
#     {"name":"철수8","age":73}
# ]

# # if랑 for만 사용해서 만들기
# result = []
# for user in users:
#     if user["age"] >= 20:
#         result.append(user)
# print(result)

# def greet(name,age):
#     print("안녕", name, age)

# greet("민수", 14)
# greet("덕배", 25)

# num1 = int(input("첫 번째 숫자 입력: "))
# any = input("기호를 입력 해 주세요: ")
# num2 = int(input("두 번째 숫자 입력: "))

# def test(a,b,c):
#     if c=='+':
#         return a+b
#     elif c=='-':
#         return a-b
#     elif c=='*':
#         return a*b
#     elif c=='%':
#         return a%b
#     elif c=='/':
#         return a/b
#     else:
#         return '잘못된 연산입니다.'

# print(test(num1,num2,any))

# def test(a):
#     return a

# print(test([1,2,3,4,5,6,7,8]))

# def test(a):
#     return a

# print(test((1,2,3,4,5,6,7,8)))

# def test(a,b='사람'):
#     return a,b

# print(test('인간',"ㄴㄴㄴ"))

# # 지역변수와 전역 변수
# # 지역 변수와 전역 변수의 차이점

# g_anyway = 0  # 전역 변수

# def any1(number):
#     #global anyway 전역 변수 선언
#     print(g_anyway, '찍을 수 있음')
#     anyway2 = 12    # 지역 변수
#     return number

# def any2(number):
#     print(g_anyway, '찍을 수 있음')
#     return number

# asd = lambda a,b: a+b
