# 스페셜 문제
# 각 입력나누기_list
data1 = input().split(',') # ['U001', '파이썬입문', '2025-03-01', '반납']
data2 = input().split(',')
data3 = input().split(',') 
data4 = input().split(',') 
data5 = input().split(',') 
data6 = input().split(',') 
data7 = input().split(',') 
data8 = input().split(',') 
data9 = input().split(',') 
data10 = input().split(',')

# 각 입력 튜플로 저장_tuple
data1_t = tuple(data1) # ('U001', '파이썬입문', '2025-03-01', '반납')
data2_t = tuple(data2)
data3_t = tuple(data3)
data4_t = tuple(data4)
data5_t = tuple(data5)
data6_t = tuple(data6)
data7_t = tuple(data7)
data8_t = tuple(data8)
data9_t = tuple(data9)
data10_t = tuple(data10)

# 전체 회원 ID를 set으로 저장
total_id = {data1[0], data2[0], data3[0], data4[0], data5[0], data6[0], data7[0], data8[0], data9[0], data10[0]}
# {'U001', 'U004', 'U003', 'U002', 'U005'}

# 책이름 list와 set으로 저장
total_book = [data1[1], data2[1], data3[1], data4[1], data5[1], data6[1], data7[1], data8[1], data9[1], data10[1]]
# ['파이썬입문', '자료구조', '파이썬입문', '알고리즘', '자료구조', '알고리즘', '데이터베이스', '알고리즘', '파이썬입문', '운영체제']
total_book_s = set(total_book)

# 각 입력데이터 도서대출 상태 list로 저장
total_state =[data1[3], data2[3], data3[3], data4[3], data5[3], data6[3], data7[3], data8[3], data9[3], data10[3]]
# ['반납', '미반납', '반납', '반납', '미반납', '반납', '미반납', '반납', '반납', '미반납']

# 회원별 대출 기록을 dict로 구성
total_data = { 
    data1[0]: [], 
    data2[0]: [], 
    data3[0]: [], 
    data4[0]: [], 
    data5[0]: [], 
    data6[0]: [], 
    data7[0]: [], 
    data8[0]: [], 
    data9[0]: [], 
    data10[0]: [] 
}
total_data[data1[0]].append(data1_t) 
total_data[data2[0]].append(data2_t) 
total_data[data3[0]].append(data3_t) 
total_data[data4[0]].append(data4_t) 
total_data[data5[0]].append(data5_t) 
total_data[data6[0]].append(data6_t) 
total_data[data7[0]].append(data7_t) 
total_data[data8[0]].append(data8_t) 
total_data[data9[0]].append(data9_t) 
total_data[data10[0]].append(data10_t)
"""{
'U001': [('U001', '파이썬입문', '2025-03-01', '반납'), ('U001', '자료구조', '2025-03-03', '미반납'), ('U001', '알고리즘', '2025-03-06', '반납')], 
'U002': [('U002', '파이썬입문', '2025-03-02', '반납'), ('U002', '알고리즘', '2025-03-05', '반납')], 
'U003': [('U003', '알고리즘', '2025-03-01', '반납'), ('U003', '자료구조', '2025-03-04', '미반납')], 
'U004': [('U004', '데이터베이스', '2025-03-01', '미반납'), ('U004', '파이썬입문', '2025-03-02', '반납')], 
'U005': [('U005', '운영체제', '2025-03-07', '미반납')]
}"""

# # step2
# print(f"""전체 대출 기록 수:{len(total_list)}
# 전체 회원 수:{len(total_id)}
# 전체 도서 종류 수:{len(set(total_book))}
# 반납 기록 수:{total_state.count("반납")}
# 미반납 기록 수:{total_state.count("미반납")}""")

# step3
user_keys = list(total_data.keys()) # 딕셔너리 키만 받기
# ['U001', 'U002', 'U003', 'U004', 'U005']

user_record1 = list(total_data[user_keys[0]]) 
# [('U001', '파이썬입문', '2025-03-01', '반납'), ('U001', '자료구조', '2025-03-03', '미반납'), ('U001', '알고리즘', '2025-03-06', '반납')]
user_record2 = list(total_data[user_keys[1]])
user_record3 = list(total_data[user_keys[2]]) 
user_record4 = list(total_data[user_keys[3]]) 
user_record5 = list(total_data[user_keys[4]]) 

user_record1_1 = list(zip(*user_record1))
# [('U001', 'U001', 'U001'), ('파이썬입문', '자료구조', '알고리즘'), ('2025-03-01', '2025-03-03', '2025-03-06'), ('반납', '미반납', '반납')]
user_record2_1 = list(zip(*user_record2))
user_record3_1 = list(zip(*user_record3))
user_record4_1 = list(zip(*user_record4))
user_record5_1 = list(zip(*user_record5))

print("회원 ID", user_keys[0])
print("대출 횟수", len(user_record1))
print("반납 횟수", user_record1_1[3].count('반납'))
print("미반납 횟수", user_record1_1[3].count('미반납'))
print("도서 목록", set(user_record1_1[1]))

# step4
print(list(total_book_s)[0], total_book.count(list(total_book_s)[0]))
print(list(total_book_s)[1], total_book.count(list(total_book_s)[1]))
print(list(total_book_s)[2], total_book.count(list(total_book_s)[2]))
print(list(total_book_s)[3], total_book.count(list(total_book_s)[3]))
print(list(total_book_s)[4], total_book.count(list(total_book_s)[4]))
print(max(total_book_s,key=total_book.count))
print(min(total_book_s,key=total_book.count))

# step5
# 모든 기록을 리스트에 튜플로 저장_원본기록
total_list = [data1_t, data2_t, data3_t, data4_t, data5_t, data6_t, data7_t, data8_t, data9_t, data10_t]
"""[('U001', '파이썬입문', '2025-03-01', '반납'), ('U001', '자료구조', '2025-03-03', '미반납'), ('U002', '파이썬입문', '2025-03-02', '반납'), 
('U003', '알고리즘', '2025-03-01', '반납'), ('U003', '자료구조', '2025-03-04', '미반납'), ('U002', '알고리즘', '2025-03-05', '반납'), 
('U004', '데이터베이스', '2025-03-01', '미반납'), ('U001', '알고리즘', '2025-03-06', '반납'), ('U004', '파이썬입문', '2025-03-02', '반납'), 
('U005', '운영체제', '2025-03-07', '미반납')]"""
# 정렬된 기록
total_list_s1 = sorted(total_list)
total_list_s1.sort(key = lambda x:x[2])
"""[('U001', '파이썬입문', '2025-03-01', '반납'), ('U003', '알고리즘', '2025-03-01', '반납'), ('U004', '데이터베이스', '2025-03-01', '미반납'), 
('U002', '파이썬입문', '2025-03-02', '반납'), ('U004', '파이썬입문', '2025-03-02', '반납'), ('U001', '자료구조', '2025-03-03', '미반납'), 
('U003', '자료구조', '2025-03-04', '미반납'), ('U002', '알고리즘', '2025-03-05', '반납'), ('U001', '알고리즘', '2025-03-06', '반납'), 
('U005', '운영체제', '2025-03-07', '미반납')]"""

total_list_s2 = list(total_list)
total_list_s2.sort(key = lambda x:(x[3]=='미반납'))
print("미반납 기록:", total_list_s2[total_state.count("반납"):])
print("반납 기록:", total_list_s2[:total_state.count("반납")])