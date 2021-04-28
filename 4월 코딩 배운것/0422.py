# numbers = []
# i = 0
# while i <= 10:
#     numbers.append(i)
#     i = i + 1
# print(numbers)

# i = len(numbers) - 1
# while i >= 0:
#     if i % 2 == 1:
#         del numbers[i]  # 인덱스 자리를 삭제
#     i -= 1
# print(numbers)

# numbers.insert(0, 20)
# print(numbers)

# numbers.remove(20)
# print(numbers)

# print(numbers.index(4))

# numbers.sort(reverse=True)
# print(numbers)


# a = [i for i in range(10)]
# print(a)

# b = list(i for i in range(10))
# print(b)

# a = [i for i in range(10) if i % 2 == 0]
# print(a)

# b = [i + 5 for i in range(10) if i % 2 == 1]
# print(b)

# a = [i*j for j in range(2, 10) for i in range(1, 10)]
# print(a)

# a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)

# a = list(map(int, a))
# print(a)

# a = list(map(str, range(10)))
# print(a)

# a = list(map(int, '12345'))
# print(a)

# b = list(map(float, "12345"))
# print(b)

# c = list(map(str, "12345"))
# print(c)

# x = input().split()
# m = map(int, x)
# a, b = m

# a = input().split()
# print(a)

# b = map(int, input().split())
# print(list(b))

# print(m)
# print(type(x))
# print(type(m))
# print(type(a))

# a = (38, 21, 53, 62, 62, 19, 53)
# print(a.index(53))

# a = (10, 20, 30, 15, 20, 40)
# print(a.count(20))

# a = (38, 21, 53, 62, 19)
# for i in a:
#     print(i, end=' ')

# print()

# i = 0
# while i < len(a):
#     print(a[i], end=' ')
#     i = i + 1

# a = tuple(i for i in range(10) if i % 2 == 0)
# print(a)

# a = (i for i in range(10) if i % 2 == 0)
# print(a)

# a = ['alpha', 'bravo', 'charlire', 'delta',
#      'echo', 'foxtrot', 'golf', 'hotel', 'india']
# b = []
# for i in a:
#     if len(i) == 5:
#         b.append(i)
# print(b)

# a, b = map(int, input().split())
# li = []
# for i in range(a, b+1):
#     if 2**i:
#         z = 2**i
#         li.append(z)
#         i += 1
# del li[1]
# del li[-2]
# print(li)

import random

for i in range(10):
    lotto = []
    while len(lotto) < 7:
        ran = random.randint(1, 51)
        if ran not in lotto:
            lotto.append(ran)
    print(lotto)

# for i in range(10):
#     lotto = random.sample(range(1, 50), 7)
#     print(lotto)

# a = (1.2, 2.5, 3.7, 4.6)
# a = tuple(map(int, a))
# print(a)

# a = (38, 21, 53, 62, 19)
# print(min(a))
# print(max(a))
# print(sum(a))

# a = ['alpha', 'bravo', 'charlire', 'delta',
#  'echo', 'foxtrot', 'golf', 'hotel', 'india']
# b = [i for i in a if a[i] >= len(5)]
# print(b)

# b = [s for s in a if len(s) == 5]
# print(b)

# a, b = int(input().split())
# user = []
# for i in range(a, b):
#     if i ** 2:
#         user.append[i]
#         del user[1]
#         del user[-1]
#         i += 1
# print(user)

# TODO 다시 해보기
# a, b = map(int, input().split())
# for i in range(a, b):
#     if i ** 2:
#         user = []
#         i = user
#         user.append[i]
#         del user[1]
#         del user[-1]
#         i += 1
# print(user)

# a, b = map(int, input().split())
# mylist = [2**i for i in range(a, b+1)]
# del mylist[1]
# del mylist[len(mylist)-2]
# print(mylist)

# import random
# r = random.randint(1, 50)
# s = [i for i in range(10)
#      for i in r
#      if len(i) < 8]
# print(s)

# TODO 로또10번 돌게 만들기
# import random
# d = []
# r = random.randint(1, 50)
# for i in range(7):
#     if r in d:
#         r = random.randint(1, 50)
#     d.append(r)
# d.sort()
# print(d)

# 답안 왜 열번이 안돌지?
# import random

# for i in range(10):
#     lotto = []
#     while len(lotto) < 7:
#         r = random.randint(1, 50)
#         if r not in lotto:
#             lotto.append(r)
# print(lotto)
# d.sort()
# print(lotto)

# import random
# for i in range(10):
#     lotto_numbers = random.sample(range(1, 51), 7)
#     lotto_numbers.sort()
#     print(lotto_numbers)

# import random
# for i in range(10):
#     l = list(range(1, 51))
#     lotto_numbers = []
#     for x in range(7):
#         r = random.choice(l)
#         l.remove(r)
#         lotto_numbers.append(r)
#     print(lotto_numbers)
#     lotto_numbers.sort()
# print(lotto_numbers)

# 2차원리스트다!!

# a = [[10, 20], [30, 40], [50, 60]]
# print(a)

# print(a[0][0]) #10
# print(a[0][1]) #20
# print(a[0][2]) #노
# print(a[1][1]) #40
# print(a[2][1]) #60
# print(a[2][2]) #노
# print(a[1][0]) #30


# a[0][1] = 1000
# print(a[0][1])

# for aa in a:
#     for aaa in aa:
#         print(aaa, end=' ')
#     print()

# for x, y in a:
#     print(x, y)

# a = [[10, 20], [30, 40], [50, 60]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# i = 0
# while i < len(a):
#     x, y = a[i]
#     print(x, y)
#     i += 1

# TODO 다시 안보고 짜보기
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         print(a[i][j], end=' ')
#         j += 1
#     print()
#     i += 1

# TODO while문으로도 짜보기
# a = [[1, 2, 3], [5, 6, 7], [8, 9, 10], [12, 13, 14]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# a = []

# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
# print(a)

a = [[1, 2, 3], [5, 6, 7], [8, 9, 10], [12, 13, 14]]

# i = 0
# for i in range(len(a)):
#     j = 0
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1
# from time import sleep
# for i in range(100):
#     msg = '\r 진행률%d%%'%(i+1)
#     print(''*len(msg), end='')
#     print(msg,end='')
#     sleep(0.1)

# def add_number(n1, n2):
#     ret = n1 + n2
#     return ret


# ans = add_number(10, 15)
# print(ans)


# def add_txt(t1, t2):
#     print(t1, t2)


# text1 = '대한민국~'
# text2 = '만세'
# add_txt(text1, text2)
