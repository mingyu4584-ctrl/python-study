# # 상속 상속 + init = super()는 세트
# class Parent: # 부모
#     def __init__(self, x):
#         self.x = x

# class Child(Parent):
#     def __init__(self, x):
#         super().__init__(x)  # 부모 클래스의 생성자 실행 부모 변수 초기화 
#         # self.y = y # 자식 클래스 전용 변수

# # c = Child()
# # print(c.a)  # 실행 가능
# # # 자식 __init__가 부모 것을 덮어씀
# # # 부모 초기화가 실행되지 않음
# # print(c.b)

# p = Parent(10)
# c = Child(5)
# # print(c.x)
# print(p.x)


# 추상 클래스 vs 일반 클래스
# 일반 클래스 -> 바로 써도 되는 완제품
# 추상 클래스 -> 혼자 쓰면 안 되는 설계도

# 현실 비유 (자판기)
# 일반 클래스
# - 버튼 누르면 바로 음료 나옴
# - 바로 사용 가능

# 추상 클래스
# - 버튼 이름만 적힌 판
# - 안에 기계 없음
# - 직접 사용 불가

from abc import ABC, abstractclassmethod

# 일반 클래스 (완제품)
class Dog:
    def sound(self):
        print("멍멍")

d = Dog()   # 바로 사용 O
d.sound()   # Os

# 특징
# - 바로 객체 생성 가능
# - 함수가 다 완성됨

# 추상 클래스 (완제품)
class Animla(ABC):
    @classmethod
    @abstractclassmethod
    def sound(self):
        pass

a = Animla()    # 에러!
# 특징
# - 직접 사용 X
# - "이 함수 꼭 만들어라" 규칙만 있음










