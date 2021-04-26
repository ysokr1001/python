# 일주일 동안 했던거 복습

# 그대로 출력하면 튜플, list를 입력하면 list로 출력됨
# r = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(list(r[:7:2]))

# 연습문제
# year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
# population = [111, 222, 333, 444, 555, 666, 777, 888]
# print(year[-3:])
# print(population[-3:])

# n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 14, 2
# print(n[1::2])

# x = input().split()
# del x[-5:]
# print(x)

# x = input().split()
# print(x[::2] + x[1::2])
# print()

# 짝수 홀수 각각 출력 - split이 없으면 z가 출력이 안됨.
# x = input().split()
# y = input().split()
# # print(x)
# # print(y)
# print(x[1::2])
# print(y[::2])
# z = x[::2] + y[1::2]
# print(z)

# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# print(Fruits.values())

# 딕셔너리를 만드는 여러가지 방법
# 1. 키=값 -> 키는 딕셔너리를 만들고 나면 문자열로 바뀜
# lux = dict(health=490, mana=334, melee=550, armor=18.72)
# print(lux)

# 2. zip사용 키 리스트와 값 리스트 병합
# lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
# print(lux2)

# 3. 리스트 안에 (키, 값)형식의 튜플 나열
# lux3 = dict([('health', 490), ('mana', 334), ('melee', 550)])
# print(lux3)

# 4. dict 안에서 중괄호로 딕셔너리 생성
# lux4 = dict({'health': 490, 'mana': 334})
# print(lux4)

# user = str(input("과일 이름을 입력하세요"))
# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# x = Fruits[user]
# print("선택한", user, "의 가격은", x, "입니다")

# 값 바꾸기
# Fruits['apple'] = 2000
# print(Fruits)

# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# print("변경전 딕셔너리를", Fruits, "입니다")
# user = int(input("변경된 사과 가격을 입력하세요"))
# Fruits['apple'] = user
# print("변경된 딕셔너리는", Fruits, "입니다")

# print(len(Fruits))

# print('banana' in Fruits)

# Fruits['tomato'] = 400
# print(Fruits)

# a = int(input("사과의 가격"))
# a1 = int(input("바나나의 가격"))
# a2 = int(input("오렌지의 가격"))
# a3 = int(input("파인애플의 가격"))
# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# Fruits['apple'] = a
# Fruits['banana'] = a1
# Fruits['orange'] = a2
# Fruits['pineapple'] = a3
# print("변경된 과일의 가격은 사과", a, "banana는", a1,
#       "orange", a2, "pineapple은", a3, "입니다")

# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# a, b, c, d = map(int, input("과일의 가격을 순서대로 입력하세요").split('/'))
# Fruits['apple'] = a
# Fruits['banana'] = b
# Fruits['orange'] = c
# Fruits['pineapple'] = d
# print(Fruits)

# print(Fruits['apple'])
# print(Fruits['orange'])

# d = dict(zip(['health', 'mana'], [200, 300]))
# print(d)

# a = input("과일을 입력하세요").split('/')
# a1 = int(input("가격을 입력하세요").split())
# a1 = map(int, input("가격").split('/'))
# a1 = map(float, input("가격").split('/'))
# b = dict(zip(a, a1))
# print(b)

# a = int(input("값"))
# if a == 7:
#     print("행운")

# i = int(input("값"))
# if i >= 10:
#     print("10이상입니다")
#     if i == 15:
#         print("15입니다")
#     if i == 20:
#         print("20입니다")

# i = int(input("값"))
# if i != 10:
#     print("10이 아닙니다")

# a = int(input("금액을 넣으세요"))
# c = str(input("쿠폰을 입력하세요"))
# if c == 'cash5000':
#     print("지불금액은:", a-5000, "입니다")
# if c == 'cash3000':
#     print("지불금액은:", a-3000, "입니다")

# user = int(input("값을 입력하세요:"))
# if user % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# user = int(input("값을 입력하세요:"))
# if user > 10:
#     print("10보다큽니다")
# if user < 10:
#     print("10보다 작습니다")
# if user == 10:
#     print("10과 같습니다")

# test = int(input("시험 접수를 입력하세요"))
# coding = str(input("합격여부를 입력하세요"))
# if test >= 80 and coding == 'True':
#     print("합격입니다")
# else:
#     print("불합격입니다")

# k = int(input("국어점수:"))
# e = int(input("영어점수:"))
# if k >= 90 and e >= 70:
#     print("합격입니다")
# else:
#     print("불합격입니다")

# if elif else가 어떻게 작동 되는지 보기
x = 20

if x == 30:
    print('10입니다')
elif x == 20:
    print('20입니다')
else:
    print('30이 아닙니다')

if x == 30:
    print('30입니다')
elif x == 20:
    print('또 20입니다')
else:
    print("30아닌데여")
