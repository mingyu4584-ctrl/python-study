students = [
    {"name": "김철수", "grade": 1, "scores": [85, 90, 88]},
    {"name": "이영희", "grade": 2, "scores": [70, 75, 72]},
    {"name": "박민수", "grade": 1, "scores": [95, 92, 93]},
    {"name": "최지은", "grade": 3, "scores": [60, 65, 58]},
    {"name": "정다은", "grade": 2, "scores": [88, 84, 90]},
    {"name": "한유진", "grade": 3, "scores": [100, 100, 100]}
]
name = []
grade = []
mean = []
rank = []

for i in students:
    n = i
    name.append(n["name"])

for i in students:
    grade.append(i["grade"])

# (1) 평균 계산 소수점 둘째 자리 반올림
def get_average(scores):
    m = []
    for i in scores:
        n = i["scores"]
        avg = sum(n)/len(n)
        m.append(round(avg,2))
    return m
mean = get_average(students)

# (2) 등급 계산
def get_grade(avg):
    r = []
    for i in avg:
        if i >= 90:
            r.append("A")
        elif i >= 80:
            r.append("B")
        elif i >= 70:
            r.append("C")
        elif i >= 60:
            r.append("D")
        else:
            r.append("F")
    return r
rank = get_grade(mean)

# (3) 전체 학생 출력
total = list(zip(name,grade,mean,rank))
for i in total:
    print(*i)

# (4) 학년별 학생 조회 결과 없으면 메시지 출력
def print_by_grade(students, grade):
    g = []
    n = []
    for i in students:
        if grade == i["grade"]:
            g.append(i["grade"])
            n.append(i["name"])
        else:
            print("")
    return list(zip(g,n))
d = print_by_grade()
