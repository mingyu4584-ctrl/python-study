# # 실습1
# class Book:
#     def __init__(self, title, author, total_pages, current_page=0):
#         self.title = title
#         self.author = author
#         self.total_pages = total_pages
#         self.current_page = current_page

#     def read_page(self, pages):
#         self.current_page += pages
#         if self.current_page < self.total_pages:
#             print(f"{self.current_page} 페이지")
#         else:
#             self.current_page = self.total_pages
#             print(f"{self.total_pages} 페이지")
            

#     def progress(self):
#         print(f"{round((self.current_page/self.total_pages)*100,1)}% ")
# book1 = Book("zzz","zzz",50,3)
# book1.read_page(30)
# book1.progress()

# # 실습1-2
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         print(self.height*self.width)

# width = int(input("가로: "))
# height = int(input("세로: "))

# R = Rectangle(width, height)
# R.area()

# 실습2
class User:
    total_users = 0
    def __init__(self, username, points=0):
        self.username = username
        self.points = points
        User.total_users += 1

    def add_points(self, amount=0):
        self.points += amount
        print(f"{self.username}의 점수: {self.points}")
    
    def get_level(self):
        if self.points >= 500:
            return "Gold"
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"
        
    @classmethod
    def get_total_users(cls):
        print(cls.total_users)
user1 = User("A")
user2 = User("B",516)
user1.add_points()
user1.add_points(256)
print(user1.get_level())
User.get_total_users()

