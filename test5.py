# # class 예시
# class Box:  # Box는 상자를 만든다
#     def __init__(self, name):   # 상자를 만드는 순간에 자동으로 실행되는 코드 name = 상자에 넣을 값
#         self.name = name    # 이 상자 안에 name을 넣어라

#     def show(self): # 상자 안에 있는 걸 보여주는 버튼 하나
#         print(self.name)    # 상자 안에 있는 name 출력
    
#     def showprint(self):
#         print(f"{self.name} 입니다.")

# a = Box("사과")
# b = Box("바나나")

# a.show()
# a.showprint()

# # class 없는 경우
# # 학생 2명의 이름과 점수 관리

# name1 = "철수"
# score1 = 90

# name2 = "영희"
# score2 = 75
# # 학생이 늘어나면 name3, score3 .... 계속 생김
# # 관련 된 값이 흩어져 있음
# # 실수 하기 쉬움

# # 클래스 사용시
# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

#     def show(self):
#         print(self.name, self.score)

# s1 = Student("철수",90)
# s2 = Student("영희",75)

# s1.show()

# # 학생이 늘어나도 같은 형식
# # 이름 + 점수 한 덩어리
# # 코드 읽기 쉽다

# # 클래스 사용 x : 비닐봉지에 물건 다 따로
# # 클래스 사용 o : 박스에 물건 정리

# class ClassName:
#     def __init__(self,p1,p2,p3):
#         self.num1 = p1
#         self.num2 = p2
#         self.num3 = p3

#     def show(self):
#         print(self.num1,self.num2,self.num3)

# # 여러명의 학생 점수를 저장하고
# # 합격/불합격을 판단해서 출력하기

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
    
#     # 확인 함수 만들기 60 이상 합격 60미만 불합격
#     def check(self):
#         if self.score >= 60:
#             print(f"{self.name} 합격")
#         else:
#             print(f"{self.name} 불합격")

# students = [
#     Student("철수", 70),
#     Student("영희", 55),
#     Student("민수", 90)
# ]

# # 출력 하기 for문 사용
# for i in students:
#     i.check()

# # 인슽턴스 변수 vs 클래스 변수 (비교)
# class Student:
#     #==========
#     # 클래스 변수
#     #===========
#     # 클래스 바로 아래에 만들면 "클래스 변수"
#     # 모든 객체(인스턴스)가 "공유"하는 변수 like 전역변수 느낌
#     school = "파이썬 고등학교"

#     def __init__(self, name, score):
#         #==========
#         # 인스턴스 변수
#         #===========
#         # self.변수 형태 -> 인스턴스 변수
#         # 객체 하나하나가 "각자 따로" 가지는 변수
#         self.name = name    # 학생마다 이름 다름
#         self.score = score  # 학생마다 점수 다름

# s1 = Student("철수",90)
# s2 = Student("영희",70)
# print(s1.name)  # 철수
# print(s2.name)  # 영희
# print(s1.score) # 90
# print(s2.score) # 70

# s1.score = 100

# print(s1.score) # 100
# print(s2.score) # 70 (영희는 영향 없음)

# s1.school = "자바 고등학교" # 가능 ? 클래스 변수를 바꾼게 아님 s1에 새 인스턴스 변수가 생긴 것

# print(s1.school)    # 자바 고등학교
# print(s2.school)    # 파이썬 고등학교

# Student.school = '자바 고등학교' # 올바른 클래스 변수 변경 방법

# print(s1.school)    # 자바 고등학교
# print(s2.school)    # 자바 고등학교

# # 왜 이런 차이가 생길까?
# # 접근 순서 (매우 중요)
# # 1 객체 안에 변수 있나?
# # 2 없으면 클래스에서 찾음

# print(s1.school)
# # s1 안에 school 있음 ? x
# # Student 안에 school 있음 ? o -> ㅇㅋ 사용

# 인스턴스 메서드 vs 클래스 메서드 (비교)

class Student:
    school = "파이썬 고등학교"
    def __init__(self, name, score):
        self.name = name
        self.score = score
    #=================
    # 인스턴스 메서드
    #===================
    def show(self):
        # self -> 이 메서드를 호출한 "객체 자신"
        # 인스턴스 변수 사용 가능
        print(self.name, self.score, Student.school)
    #=================
    # 클래스 메서드
    #=================
    @classmethod
    def change_school(cls, new_school):
        # cls -> 클래스 자신 (Student)
        # 인스턴스 변수(self.xxx)는 사용 x
        # 클래스 변수만 사용 o
        cls.school = new_school
    #=================
    # 스태틱(정적) 메서드
    #=================
    @staticmethod
    # self x
    # cls x
    # 클래스 안에 있지만 
    # 클래스/객체 정보 전혀 안씀
    # 그냥 "관련 있는 함수"를 묶어둔 것
    def is_pass(score):
        if score >= 60:
            return "합격"
        else:
            return "불합격"

s1 = Student("철수",90)
s2 = Student("영희",70)

# 인스턴스 메서드 사용
# 각 객체의 값 사용
s1.show()
s2.show()

# 클래스 메서드 사용
# 모든 객체에 영향
Student.change_school("자바 고등학교")
s1.show()
s2.show()

#스태틱(정적) 메서드 사용
print(Student.is_pass(80))
print(s1.is_pass(80))   # 사용가능 -> 권장 하지 않음


# 절대 헷갈리면 안 되는 차이
# 클래스 메서드에서 이건 안됨
# @classmethod
# def wrong(cls):
#     print(self.name) # X self 없음 -> 에러

# # 인스턴스 메서드에서 클래스 변수 변경 x
# def wron(self):
#     self.school = "c언어 고등학교" # X 인스턴스 변수 새로 생김


# 접근 기준 (이거 외우면 그냥 끝)
# self -> 한명
# cls -> 전체

# 한눈에 비교
# 구문              인스턴스 메서드             클래스 메서드
# 첫 번째 인자       self                       cls
# 호출 방법         객체.메서드()                클래스.메서드()
# 접근 가능         인스턴스 + 클래스            클래스만
# 용도              개인행동                    전체 설정 
# 예시              점수출력                    학교변경 

# 최종 요약
# 인스턴스 메서드 = 개인용
# 클래스 메서드 = 공용 설정용

# 스태틱(정적) 메서드 핵심 주의점
# 의미 없는 행동 예시
# @staticmethod
# def wrong(self):
#     print(self.name)    # 접근 불가

# 스태틱(정적) 메서드 언제 사용?
# 클래스/객체 상태를 전혀 모를 때만 사용

# 언제 어떤 메서드 쓰냐?
# self 필요 -> 인스턴스 메서드
# cls 필요 -> 클래스 메서드
# 둘 다 필요 x -> 스태틱(정적) 메서드

# 비유 예시
# 인스턴스 메서드 -> 학생 개인 행동
# 클래스 메서드 -> 학교 규칙 변경
# 스태틱 메서드 -> 계산기

# 결론
# 스태틱 메서드느 "클래스랑 관련은 있지만 상태는 필요 없는 함수 (도우미)"


