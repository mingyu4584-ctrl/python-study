class MoneyItem:
    def __init__(self, day, name, money, inf):
        self.day = day
        self.name = name
        self.money = money
        self.inf = inf
    
    def show(self):
        print(f"[{self.day}] {self.name}: {self.money}원 ({self.inf})")

items =[]

while True:
    m = int(input("메뉴입력(1~6): "))
    income = 0
    expense = 0
    if m == 1:  # 내역 추가
        day = input("날짜 입력: ")
        name = input("이름 입력: ")
        money = int(input("금액 입력: "))
        inf = input("종류(수입/지출): ")
        new_item = MoneyItem(day, name, money, inf)
        items.append(new_item)
    elif m == 2:    # 전체 내역 보기
        for i in items:
            i.show()
    elif m == 3:    # 총 수입 / 총 지출 / 잔액 보기
        for i in items:
            if i.inf == "수입":
                income += i.money
            else:
                expense += i.money
        total = income - expense
        print(f"총 수입: {income}원 / 총 지출: {expense}원 / 잔액: {total}")
    elif m == 4:    # 특정 금액 이상 지출 보기
        s = int(input("특정 금액 이상 지출: "))
        for i in items:
            if i.inf == "지출" and i.money >= s:
                i.show()
    elif m == 5:    # 특정 날짜 내역 보기
        d = input("특정 날짜 내역: ")
        for i in items:
            if i.day == d:
                i.show()
    else:   # 프로그램 종료
        print("종료")
        break

