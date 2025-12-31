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

# # 실습2
# intro = '둠칫'
# drop = '두둠칫'

# print(intro + drop*3)

# # 사용자 입력
# x = input('아무 숫자나 입력:')
# print(x)

# name = input('이름을 입력:')
# print('안녕하세요', name)

# score = int(input('점수를 입력:'))
# print(f'입력한 점수는 {score}점')

# name = input('이름을 입력:')
# score = int(input('점수를 입력:'))

# print(f'이름은 {name}')
# print(f'입력한 점수는 {score}점')

# a = int(input('첫 번째 값:'))
# b = int(input('두 번째 값:'))

# print(a+b)

# fruit = '사과 참외 수박'.split()
# print(fruit)

# s1, s2, s3 = input().split()
# print(s1, s2, s3)

# # 실습3
# name = input('이름 :')
# age = int(input('나이:'))
# print(f'안녕하세요. 저는 {name}이고, {age}살입니다.')

# # 실습4-1
# row = int(input('가로:'))
# col = int(input('세로:'))

# print('넓이:',row*col)
# print('둘레:',2*(row+col))

# # 실습4-2
# num = int(input("4자리 정수 입력: "))
# a = num/1000
# b= (num/100)%10
# c = (num/10)%10
# d = (num%10)
# print("천의 자리: ", int(a))
# print("백의 자리: ",int(b))
# print("십의 자리: ", int(c))
# print("일의 자리: ", int(d))

# # 실습5
# year, month, day = input("날짜를 입력:").split('.')
# hour, min, sec = input("시간을 입력:").split(':')
# print(f"""RE3의 개강일은 {year}년 {month}월 {day}일
# 시작 시간은 {hour}시 {min}분 {sec}초 입니다.""")

# # list
# sample_list = ['s','f','a',5]
# print(sample_list[2])
# print(len(sample_list))

# list1 = list()

# # 문자열을 리스트로
# strlist = list('codingOn')

# print(list1, '첫번째 확인')
# print(strlist, '데이터 값 들어온거 확인용')

# sample = [51,15,5,846,1,8,6,61,26,5165]

# print(sample[int(len(sample)/2)])

# fruits = ['appel', 'banana', 'cherry']
# fruits[0] = 'orange'
# print(fruits[0])

# # slicing
# nums = [10,20,30,40,50,60,70,80,90]
# print(nums[-4:-2])
# print(nums[::-1]) #뒤집기

# # 실습1
# nums = [10,20,30,40,50]
# print(nums[0],nums[-1], "실습1-1")

# nums = [100,200,300,400,500,600,700]
# print(nums[int(len(nums)/2)-1:int(len(nums)/2)+2], "실습1-2")

nums = [1,2,3,4,5]
nums[:] = nums[:] * 2
print(nums, "실습1-3")

# items = ["a","b","c","d","e"]
# print(items[::-1], "실습1-4")

# data = ["zero","one","two","three","four","five"]
# print(data[::2], "실습1-5")

# movies = ["인셉션","인터스텔라","어벤져스","라라랜드","기생충"]
# movies[2:3] = "매트릭스","타이타닉"
# print(movies, "실습1-6")

# sub = ["국어","수학","영어","물리","화학","생물","역사","지구과학","윤리"]
# print(sub[3::2], "실습1-7")

# data = ["a","b","c","d","e","f","g","h","i"]
# print(data[2::-1],data[7:4:-1],data[:5:-1], "실습1-8")

# # 실습2
# fruits = ["appel","banana","cherry","grape","watermelon","strawberry"]
# del fruits [1:4]
# print(fruits, '실습2-1')

# letters = ["A","B"]
# letters *= 3
# del letters[int(len(letters)/2)-1]
# print(letters, "실습2-2")

# 실습3

