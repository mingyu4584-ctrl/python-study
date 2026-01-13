# 실습3-1
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password = new_pw
            return self.__password
        else:
            print("비밀번호 불일치")

    def get_check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

user1 = UserAccount("a","aaa1212")
print(user1.get_check_password("aaa1212"))
print(user1.set_change_password("aaa1212","ab123"))
print(user1.get_check_password("ab123"))

# 실습3-2
class Student:
    def __init__(self, score):
        self.__score = score
    
    @property
    def getter(self):
        return self.__score
    
    @getter.setter
    def setter(self, score):
        if 0 <= score <= 100:
            self.__score = score
            return self.__score
        else:
            print("ValueError")

s1 = Student(150)
print(s1.getter)
s1.setter = 150

# 실습4
