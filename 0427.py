# 시작 문제
# def plus(a):
#     return a + 10


# print(plus(1))

# 람다 선언해보기 TODO none이 왜 나옴?
# def plus_ten(x): lambda x: x+10


# print(type(plus_ten))
# print(plus_ten(1))

# data = (lambda x: x+10)(1)
# print(type(data))
# print(data)

# y = 10
# data = (lambda x: x + y)(1)
# print(data)

# 잘못된거 확인하기, 다른 변수가 있으면 오류가 남
# data = (lambda x: y=10
#         x + y)(1)
# print(data)

# def plus_ten(x):
#     return x + 10


# a = list(map(plus_ten, [1, 2, 3]))
# print(a)

# a = list(map(lambda x: x + 10, [1, 2, 3]))
# print(a)

# 람다로도 복잡하게 식을 표현할 수 있음
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

# 딥러닝 하다보면 함수보다 람다로 표현하는게 나을 때도 있음
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

# 위를 함수로 표현하기
# def hello(a):
#     if a == 1:
#         return str(a)
#     elif a == 2:
#         return float(a)
#     else:
#         return a + 10


# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(hello, b)))

# 두 리스트 요소를 곱해서 새 리스트 만들기
# a = [1, 2, 3, 4, 5]
# b = [2, 4, 6, 8, 10]
# print(list(map(lambda x, y: x*y, a, b)))

# 오류 나는 거 확인
# def plus(x): return x + 10
# print(lambda x: x + 10)
# print(plus)
# 아래 식을 넣으면.. TODO 람다 이해하기
# data = plus

# def f(x):
#     return x > 5 and x < 10


# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# print(list(filter(f, a)))

# #위를 람다식으로
# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# print(list(filter(lambda x: x > 5 and x < 10, a)))

# 리듀스
# from functools import reduce


# def f(x, y):
#     return x + y


# a = [1, 2, 3, 4, 5]
# print(reduce(f, a))

# 위 식을 람다로 바꾸기
# from functools import reduce
# a = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x+y, a))


# 전역변수 지역변수
# def foo():
#     x = 10
#     print(x)


# foo()
# print(x)

# 함수 안에서 전역 변수 변경

# x = 10


# def foo():
#     x = 20
#     print(x)


# foo()
# print(x)

# # 글로벌 사용 / 전역변수 x = 10이 없더라도 20, 20이 나옴
# x = 10


# def foo():
#     global x
#     x = 20
#     print(x)


# foo()
# print(x)

# 함수 안에서 함수 만들기
# def print_hello():
#     hello = 'hello, world!'

#     def print_message():
#         print(hello)
#     print_message()


# print_hello()

# 함수 안에서 함수 만들기 지역변수 변경하기
# def A():
#     x = 10

#     def B():
#         x = 20
#     B()
#     print(x)


# A()

# B안의 X를 출력하고 싶다면?!


# def A():
#     x = 10

#     def B():
#         nonlocal x
#         x = 20
#     B()
#     print(x)


# A()

# 변수 찾는 순서를 알아보자 TODO 왜 50, 400 이해하기
# def A():
#     x = 10
#     y = 100

#     def B():
#         x = 20

#         def C():
#             nonlocal x
#             nonlocal y
#             x = x + 30
#             y = y + 300
#             print(x)
#             print(y)
#         C()
#     B()


# A()


# global로 전역변수 사용하기
# x = 1


# def A():
#     x = 10

#     def B():
#         x = 20

#         def C():
#             global x
#             x = x + 30
#             print(x)
#         C()
#     B()


# A()

# 클로저 사용하기

# def calc():
#     a = 3
#     b = 5

#     def mul_add(x):
#         return a*x+b
#     return mul_add


# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))

# 위 식을 람다로 바꿔보기
# def calc():
#     a = 3
#     b = 5
#     return lambda x: a * x + b


# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))

# 클로저의 지역변수 변경하기
# def calc():
#     a = 3
#     b = 5
#     total = 0

#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add


# c = calc()
# c(1)
# c(2)
# c(3)

# 위 코드에서 nonlocal을 사용 안한경우
# def calc():
#     a = 3
#     b = 5

#     def mul_add(x):
#         total = 0
#         total = total + a * x + b
#         print(total)
#     return mul_add


# c = calc()
# c(1)
# c(2)
# c(3)


# b값을 중간에 추가해보기
# def calc():
#     a = 3
#     b = 5
#     total = 0

#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add


# c = calc()
# c(1)
# c(2)
# # c(3)
# b = calc()
# b(3)
# print("=======")
# print(b(3)) #TODO 왜 none이 나옴?


# 호출횟수를 세는 함수 만들기
# def counter():
#     i = 0

#     def count():
#         nonlocal i
#         i += 1
#         return i  # 내답 i + 1
#     return count


# c = counter()
# for i in range(10):
#     print(c(), end=' ')

# 텍스트 파일 입출력 방법을 알아봅시다
# C:\Users\ysokr\Desktop\ICT
# inFp = open("C:/Users/ysokr/Desktop/ICT/data1.txt", "r", encoding="utf-8")
# inStr = inFp.readline()
# print(inStr, end="")
# inStr = inFp.readline()
# print(inStr, end="")
# inStr = inFp.readline()
# print(inStr, end="")
# inStr = inFp.readline()
# print(inStr, end="")
# inFp.close()

# 범용? 입출력방법// 한줄씩 읽는 방법
# inFp = None
# inStr = ""
# inFp = open("C:/Users/ysokr/Desktop/ICT/data1.txt", "r", encoding="utf-8")
# while True:
#     inStr = inFp.readline()
#     if inStr == "":
#         break
#     print(inStr, end="")
# inFp.close()

# 파이썬에서 파일을 한꺼번에 읽는 방법
# inFp = open("C:/Users/ysokr/Desktop/ICT/data1.txt", "r", encoding="utf-8")
# inList = []
# inList = inFp.readlines() #s가 추가됨
# print(inList)
# inFp.close()

# 위의 코드를 한줄씩 출력하고 싶을 때?
# inFP = None
# inList = []
# inStr = ""
# inFp = open("C:/Users/ysokr/Desktop/ICT/data1.txt", "r", encoding="utf-8")


# inList = inFp.readlines()  # s가 추가됨
# for inStr in inList:
#     print(inStr, end="")
# inFp.close()

# 파일명을 입력받아 입출력해보기
# 파일명 : C:/Users/ysokr/Desktop/ICT/data1.txt

# z = input("파일명을 입력하세요")

# inFp = open(z, "r", encoding="utf-8")
# inList = []
# inList = inFp.readlines()  # s가 추가됨
# print(inList)
# inFp.close()

# 파일에 입력하는 방법 인풋 이용
# outFp = None
# outStr = ""

# outFp = open("C:/Users/ysokr/Desktop/ICT/data2.txt", "w", encoding="utf-8")

# while True:
#     outStr = input("내용입력: ")
#     if outStr != "":
#         outFp.writelines(outStr+"\n")
#     else:
#         break
# outFp.close()
# print("---정상적으로 파일에 써졌음---")

# 이미 만들어져 있는 파일을 읽어서 카피파일 만들기
outFp = None
outStr = ""
inList = []

inFp = open("C:/Users/ysokr/Desktop/ICT/data1.txt", "r", encoding="utf-8")
outFp = open("C:/Users/ysokr/Desktop/ICT/data2.txt", "w", encoding="utf-8")

while True:
    outStr = input("내용입력: ")
    if outStr != "":
        outFp.writelines(outStr+"\n")
    else:
        break
outFp.close()
print("---정상적으로 파일에 써졌음---")

#
#
# inList = inFp.readlines() #s가 추가됨
# print(inList)
# inFp.close()
