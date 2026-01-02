# # 튜플 언패킹
# a, b, c = (1, 2, 3)
# a, b, c = 4, 5, 6 # 괄호 생략
# x = (1, 2, 3) # 지정

# # 리스트 언패킹
# d, e, f = [4, 5, 6]

# # 문자열 언패킹
# g, h = 'ok'

# # 결과 출력
# print(a,b,c, '튜플 언패킹')
# print(d,e,f, '리스트 언패킹')
# print(g,h, '문자열 언패킹')

# t = (1,2,3)
# # 방법1. 첫 번째 요소를 100으로 바꾼 새로운 튜플 만들기
# new_t = (100,) + t[1:]
# print(new_t) # (100,2,3)
# # 방법2. 리스트로 변환 후 다시 변환
# temp = list(t) # 튜플을 리스트로 변환
# temp[1] = 200 # 리스트 수정이 가증
# t = tuple(temp) # 다시 튜플로 변환
# print(t) # (1, 200, 3)

# # 실습1
# user = ("minji",25,"Seoul")
# l_user = list(user)
# l_user[0] = "eunji"
# restored_user = tuple(l_user)
# print(restored_user,"step1")
# name, age, city = restored_user
# print(f"{name}, {age}, {city}","step2")
# if(city == 'Seoul'):
#     print("※ 서울 지역 보안 정책 적용 대상입니다.", "step3")
# else:
#     print("※ 일반 지역 보안 정책 적용 대상입니다.", "step3")
# users = ("minji","eunji","soojin","minji","minji")
# print(f""""minji"라는 이름 등장 횟수:{users.count("minji")}
# "soojin"이 처음 등장하는 위치:{users.index('soojin'[:])}""", "step4")
# l_users = list(sorted(users))
# sorted_users = tuple(l_users)
# print(l_users, "step5")

# # 집합(set)
# s1 = {1,2,3}
# s1 = {1,1,1,2,2,2,2,3,3,3,3,3,4,7,7,5,4}
# print(s1)
# s2 = set([1,2,3,2])
# print(s2)
# s = {}  # dict
# s1 = set() # set
# print(type(s), type(s1))
# s = {10,10,40,40,50,50,20,30} # set은 순서 없음 -> 리스트 변환 후 출력
# s_list = list(s)
# print(s_list[0]) # 가능은 함 다만 순서는 예측 불가능
# print(list(s)[0])
# s = {1,2,(3,4)} # 가능함 => 변경이 불가능한 객체들의 모임
# s1 = {[1,2]} # 불가능

# A = {1,2,3}
# B = {3,4,5}
# # 합집합 -> 두 집합에 들어 있는 모든 원소를 합친 것(중복 제거)
# print(A|B) # {1,2,3,4,5}
# print(A.union(B)) # {1,2,3,4,5}
# # 교집합 -> 두 집합에 공통으로 들어 있는 원소
# print(A&B) # {3}
# print(A.intersection(B)) # {3}
# # 차집합 -> A - B 뺌
# print(A-B) # {1,2}
# print(A.difference(B)) # {1,2}
# # 대칭 차집합 -> A 와 B 중에서 서로 겹치지 않는 것들만 ex) 한쪽에 있는 것들
# print(A^B) # {1,2,4,5}
# print(A.symmetric_difference(B)) # {1,2,4,5}

# #실습1
# submission = ['kim','lee','kim','park','choi','lee','lee']
# s = set(submission)
# print(f"""제출한 학생 수: {len(s)}
# 제출자 명단: {s}""", "step1")
# user1 = {'SF','Action','Drama'}
# user2 = {'Drama','Romance','Action'}
# print(f"""공통 관심 장르:{user1 & user2}
# 서로 다른 장르: {user1 ^ user2}
# 전체 장르: {user1 | user2}""", "step2")
# my_certificates = {'SQL','Python','Linux'}
# job_require = {'SQL','Python'}
# print(f"지원 자격 충족 여부: {job_require.issubset(my_certificates)}", "step3")
