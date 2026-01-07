# # 정보 은닉과 캡슐화
# # Public / Protected / Private

# class Box:
    
#     def __init__(self, name, price, secret):    # 객체가 만들어질 때 자동 실행되는 함수
#         self.name = name    # Public 변수   어디서든 접근 가능
#         self._price = price  # Protected 변수   외부 접근 가능 하지만 "건들지 말자"는 약속
#         self.__secret = secret # Private 변수   클래스 내부에서만 사용

#     def show(self): # 박스 정보 출력용 메서트 인스턴스
#         print(self.name)    # 자유롭게 접근 가능
#         print(self._price)  # 외부 접근 가능한데 권장하진 x 내부에서 ok
#         print(self.__secret)    # 클래스 내부에서만 ok

#     def get_secret(self):   # private 값을 꺼내기 위한 메서드
#         return self.__secret # 외부에서는 이 방법으로만 접근 가능!
    
# box = Box("사과박스", 1000, "비밀번호")
# print(box.name) # O public
# print(box._price) # O 단, 권장하진 않음
# # print(box.__secret) # X 에러!
# print(box.get_secret()) # 올바른 접근

# 캡슐화 
# 데이터를 직접 만지지 못하게 하고
# 메서드를 통해서만 사용하게 하는 것

# # 캡슐화 안 한 경우 (문제 있는 코드)

# class Speaker:
#     def __init__(self):
#         self.volume = 5

# sp = Speaker()
# sp.volume = 100 # x 말도 안 되는 값
# sp.volume = -10 # X 인런 것도 가능

# print(sp.volume, "확인용")

# # 캡슐화 한 경우(정석)

# class Speaker:
#     def __init__(self):
#         self.__volume = 5   # private 변수 외부 접근 차단
    
#     @property   # getter 역할 함 sp.volume으로 읽기 가능
#     def volume(self):   # 값 읽기 전용
#         return self.__volume    # private 값 반환
    
#     @volume.setter  # setter 역할 함 sp.volume = 값 형태 가능
#     def volume(self, value):    # setter (값 설정 담당)
#         if 0 <= value <= 10:    # 값을 검증
#             self.__volume = value   # 검증 통과한 값만 저장
#             # print(self.get_volume())
#         else:
#             print("볼륨은 0~10 사이만 가능 합니다.")
    
#     def play_sound(self):
#         print("소리를 재생 합니다.")

# sp = Speaker()

# print(sp.volume)    # getter 호출
# sp.volume = 8   # setter 호출
# sp.volume = 20  # X 제한됨
# # 겉보기엔 변수
# # 속은 메서드

# # 비교 정리
# # 방식                  사용법
# # 직접 접근             sp.volume X
# # getter/setter         get_volume()/set_volume()
# # @property             sp.volume O

# # 캡슐화가 그래서 뭐냐?
# # 데이터는 숨기고
# # 접근은 통제하고
# # 사용은 편하게 한다

# # @property는 
# # 캡슐화를 유지하면서
# # 변수처럼 사용하게 해준다

# sp.set_volume(20)    # 잘 변경 가능
# sp.get_volume
# # 문법이 어색함
# # 변수처럼 쓰고 싶은데 메서드 처럼 써야 함
# # property 등장 (파이썬식 해결)
# # 메서드인데 변수처럼 쓰게 해주는 문법

# # sp.__volume = 100
# # # 값 검증 불가
# # # 내부 상태 망가짐
# # # 그래서 직접 접근 x
# # # 매서드로만 접근 o

# 상속과 오버라이딩
# 상속이란?
# 기존 클래스를 물려받아서
# 기능을 그대로 쓰거나 확장 하는 것


class Speaker:  # 부모 클래스 (기본 기능)
    def __init__(self):
        self.__volume = 5   # private 변수 외부 접근 차단
    
    @property   # getter 역할 함 sp.volume으로 읽기 가능
    def volume(self):   # 값 읽기 전용
        return self.__volume    # private 값 반환
    
    @volume.setter  # setter 역할 함 sp.volume = 값 형태 가능
    def volume(self, value):    # setter (값 설정 담당)
        if 0 <= value <= 10:    # 값을 검증
            self.__volume = value   # 검증 통과한 값만 저장
            # print(self.get_volume())
        else:
            print("볼륨은 0~10 사이만 가능 합니다.")
    
    def play_sound(self):   # 모든 스피커가 공통으로 가지는 기능
        print("소리를 재생 합니다.")

# 오버라이딩
# 부모 메서드를
# 자식 클래스에서 다시 만드는 것

class SmartSpeaker(Speaker): # 이 한 줄이 상속 Speaker 기능 전부 물려받음

    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def play_sound(self):   # 부모의 play_sound를 덮어씀
        super().play_sound()    # 부모 클래스 메서등 호출
        print("AI가 추천한 음악을 재생합니다.") # 자신만의 동작

# smart = SmartSpeaker()
# smart.play_sound()
# print(smart.volume)

# normal = Speaker()
smart = SmartSpeaker()

# normal.play_sound()
smart.play_sound()
# 같은 메서드
# 객체에 따른 다른 동작






















































