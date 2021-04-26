# hello 100번 출력하기 TODO 이렇게 하면 안되나? 아래는 정답
def hello(count):
    for i in range(count):
        print('Hllo, world!')


hello(3)


# def hello():
#     print('Hello, world!')


# for i in range(100):
#     hello1()


# def add(a, b):
#     print(a + b)


# add(10, 20)


# def add(a, b):
#     return a + b


# x = add(10, 20)
# print(x)

# def add(a, b):
#     return a+b


# print(add(10, 20))

# 값을 받아서 함수 사용하기
# def add(a, b, c):
#     return a*b*c

# a, b, c, = map(int, input().split())
# print(add(a, b, c))

# 함수에서 값을 여러 개 반환하기

# def add_sub(a, b):
#     return a+b, a-b


# x, y = add_sub(10, 20)
# print(x)
# print(y)


# x = add_sub(10, 20)
# print(x)

# x, y = (30, -10)
# print(x)
# print(y)

# def hello(a, b):
#     return a+b, a-b


# a, b = hello(10, 20)
# print(type(a))
# z = hello(10, 20)
# print(type(z))

# print()
# c, d = z
# print(z, c, d)

# def hello(a, b):
#     return a+b, a-b, a*b, a/b


# a, b = map(int, input().split())
# x, y, g, z = hello(a, b)

# print("%d * %d = " % (a, b), z)
# print("+=%.2f, -=%.2f, *=%.2f, /=%.2f" % (x, y, g, z))

# 함수의 호출과정 알아보기
# def mul(a,b):
#     c = a*b
#     return c

# def add(a,b):
#     c = a+b
#     print(c)
#     d = mul(a,b)
#     print(d)

# x = 10
# y = 20
# add(x,y)

# x = 10
# y = 3


# def get_quetient_remainder(a, b):
#     return a//b, a % b


# quotient, remainder = get_quetient_remainder(x, y)
# print('몫:{0}, 나머지: {1}'.format(quotient, remainder))

# 표준입력 두개 숫자, 연산자 결과 출력
# x, y = map(int, input().split())


# def calc(x, y):
#     return x+y, x-y, x*y, x/y


# a, s, m, d = calc(x, y)
# print('덧셈:{0}, 뺄셈:{1}, 곱셈:{2}, 나눗셈:{3}'.format(a, s, m, d))


# 함수 계산기 = 5개의 함수

# def plus(x, y):
#     return x+y


# def minus(x, y):
#     return x-y


# def times(x, y):
#     return x*y


# def divided_by(x, y):
#     return x/y


# def remainder(x, y):
#     return x % y


# while True:
#     c = int(input("원하는 연산자를 입력하세요:1.더하기, 2빼기, 3곱하기, 4나누기, 5나머지, 6나가기"))
#     if c <= 5:
#         x = int(input("첫번째 숫자를 입력하세요"))
#         y = int(input("두번째 숫자를 입력하세요"))
#         if c == 1:
#             result = plus(x, y)
#             print(result)
#         elif c == 2:
#             result = minus(x, y)
#             print(result)
#         elif c == 3:
#             result = times(x, y)
#             print(result)
#         elif c == 4:
#             result = divided_by(x, y)
#             print(result)
#         elif c == 5:
#             result = remainder(x, y)
#             print(result)
#     elif c == 6:
#         break
#     else:
#         print("잘못 입력하셨습니다")

# 한개의 함수 계산기
# def add(x, y):
#     return x+y, x-y, x*y, x/y, x % y


# x = int(input("첫번째 숫자를 입력하세요"))
# y = int(input("두번째 숫자를 입력하세요"))

# a, b, c, d, e = add(x, y)
# while True:
#     c = int(input("원하는 연산자를 입력하세요:1.더하기, 2빼기, 3곱하기, 4나누기, 5나머지, 6나가기"))
#     if c <= 5:
#         if c == 1:
#             print(a)
#         elif c == 2:
#             print(b)
#         elif c == 3:
#             print(c)
#         elif c == 4:
#             print(d)
#         elif c == 5:
#             print(e)
#     elif c == 6:
#         break
#     else:
#         print("잘못 입력하셨습니다")

# TODO 대성이한테 물어보기 menu안됨
# def allcal(type, a, b):
#     if type == 1:
#         return a+b
#     elif type == 2:
#         return a-b
#     elif type == 3:
#         return a*b
#     elif type == 4:
#         return a/b
#     elif type == 5:
#         return a % b


# while True:
#     menu = int(input("계산기 기능을 입력하세요"))
#     x = int(input("첫번째 숫자를 입력하세요"))
#     y = int(input("두번째 숫자를 입력하세요"))
#     result = allcal(menu, x, y)
#     print("결과는 %d입니다" % result)

# import random


# def make_question():
#     a = random.randint(0, 99)
#     b = random.randint(0, 99)
#     op = random.randint(1, 3)

#     q = str(a)
#     if op == 1:
#         q = q + "+"
#     if op == 2:
#         q = q + "-"
#     if op == 3:
#         q = q + "*"
#     q = q + str(b)
#     return q


# sc1 = 0
# sc2 = 0

# for x in range(5):
#     q = make_question()
#     print(q)
#     ans = input("=")
#     r = int(ans)

#     if eval(q) == r:
#         print("정답")
#         sc1 = sc1+1
#     else:
#         print("오답")
#         sc2 = sc2+1
#     print("정답:", sc1, "오답:", sc2)
#     if sc2 == 0:
#         print("모두 정답입니다")
