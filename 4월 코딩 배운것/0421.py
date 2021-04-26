# i = 0
# while i < 100:
#     (i ** (1/2))
#     i += 1
#     print(i)

# TODO 왜 출력이 안됨?! 합계가?
# i = 1
# line = 0
# total = 0
# while i <= 100:
#     if i % 2 == 0:
#         pass
#         total += i*i
#         print("+", i*i)
#     else:
#         total -= i*i
#         print("-", i*i)
#     i += 1
#     line += 1

#     if line == 10:
#         line = 0
#         print()
# print(total, "입니다")

# i = 0
# for i in range(100):
#     if i % i == 1:

# 내식대로 풀기 ...? 왜 안될까 다시 해보기
# t = 0
# i = 2
# line = 0
# for i in range(100):
#     j = 2
#     if i % j == 0:
#         break
#     else:
#         t = t + i
#         print(i, "입니다", end='  ')
#         line = line + 1
#         if line == 7:
#             line = 0
#             print()
#     i += 1

# append를 활용하여 요소 추가하기
# a = [10, 20, 30]
# a.append(500)
# print(a)
# print(len(a))

# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# a = []
# for i in range(10):
#     a.append((i+1)*10)
# print(a)

# 짝수 출력하기
# a = []
# for i in range(101):
#     if i % 2 == 0:
#         a.append(i)

# 리스트 안에 리스트
# a = [10, 20, 30]
# a.append([500, 600])
# print(a)
# print(len(a))

# extend는 리스트 확장개념
# a = [10, 20, 30]
# a.extend([500, 600])
# print(a)
# print(len(a))

# insert는 위치하는 자리에 넣어주는
# a = [10, 20, 30]
# a.insert(0, 5)
# a.insert(len(a), 40) #맨마지막에 넣기
# print(a)
# print(len(a))

# a = [10, 20, 30]
# a.insert(1, [500, 600])
# print(a)

# a = [10, 20, 30]
# a[1:1] = [500, 600]
# print(a)

# pop 마지막 요소, 특정 인덱스 요소 삭제
# a = [10, 20, 30]
# a.pop()
# print(a)
# a = [10, 20, 30]
# a.pop(1)
# print(a)

# remove 값 없애줌
# a = [10, 20, 30]
# a.remove(20)
# print(a)

# # 값이 여러개 있는 경우 - 하지만 첫번째 값만 날라감
# a = [10, 20, 30, 20]
# a.remove(20)
# print(a)
# a = []
# for i in range(4):
#     i += 1
#     a.append(i*10)
#     print(a)
# for i in range(4):
#     print(a.pop())

# TODO 마지막 for문 왜 30 20 으로 출력이 되는가?
# a = []
# for i in range(7):
#     i += 1
#     a.append(i*10)
#     print(a)
# a.pop()
# print(a)
# print()


# for i in range(len(a)-1):
#     print(a.pop())
#     print(a)
#     print()


# [10]
# i


# a = [10, 20, 30, 15, 20, 40]
# print(a.index(20))
# # print(a)

#a = [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
#b = []
# for i in a:
#    a.index(20)
#    print(a.index(20))
#    a.remove()
# print(b)

# i = 0
# a = [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
# result = []
# while True:
#    if 20 in a:
#        ni = a.index(20)
#        result.append(ni+i)
#        a.pop(ni)
#        i += 1
#    else:
#        break
# print(result)

# 답은 1 4 6 10인데 1 3 4 7이 출력?
# for i in a:
#     if i == 20:
#         z = a.index(20)
#         result.append(z)
#         a.pop(z)
# print(result)

# 내가 하고 싶었던 게 이거여써
# for i in range(len(a)):
#     if a[i] == 20:
#         result.append(i)
# print(result)

# a = [10, 20, 30, 15, 20, 40]
# print(a.count(20))
# a.reverse()
# print(a)

# 작은 값부터 큰 값으로
# a.sort()
# print(a)

# 내림차순
# a.sort(reverse=True)
# print(a)

# 모든 요소 삭제 - 두가지 방법
# 첫번째
# a.clear()
# print(a)

# 두번째
# del a[:]
# print(a)

# 왜 len이 바뀌면 500만 출력될까?
# a = [10, 20, 30]
# a[len(a):] = [500]
# print(a)

# a = [10, 20, 30]
# a[:len(a)] = [500, 600]
# print(a)

# b는 a의 주소를 갖게 되는 것, b리스트를 따로 복제해서 가지고 있는 것이 아님
# a = [0, 0, 0, 0, 0]
# b = a
# print(a)
# print(b)

# print(a is b) #True

# b[2] = 99
# print(a)
# print(b)  #[0, 0, 99, 0, 0] 똑같이 출력

# 아예 a리스트를 복제하고 싶을 때
# a = [0, 0, 0, 0, 0]
# b = a.copy()
# a is b
# print(a is b)
# print(a == b)

# b[2] = 99
# print(a)  # 0, 0, 0, 0, 0
# print(b)  # 0, 0, 99, 0, 0

# a = [38, 21, 53, 62, 19]
# for i in a:
#     print(i)

# for index, value in enumerate(a):
#     print(index, value)

# for index, value in enumerate(a, start=1):
#     print(index, value)

# 실패
# a = [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
# result = []
# for i in range(len(a)):
#     i == 20
#     if z, x in enumerate(a):
# print(z, 0)

# for i, value in enumerate(a):
#     if value == 20:
#         result.append(i)
# print(result)

# a = [38, 21, 53, 62, 19]

# i = 0
# while i < len(a):
#     i == a
#     print(i)

# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# lar = a[0]
# for i in a:
#     if i > lar:
#         lar = i
# print(lar)

# s = a[0]
# for i in a:
#     if i < s:
#         s = i
# print(s)

# a.sort()
# print(a[0])

# a.sort(reverse=True)
# print(a[0])

# m = max(a)
# print(m)
# print(max(a))
# print(min(a))

# print(sum(a))

# 왜 안되징
# n = []
# n.append[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(n)

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# for i in n:
#     if i % 2 == 1:
#         z = i
#     del n[z]
# print(n)

# TODO 되게 만들기
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# for i in n:
#     if i % 2 == 1:
#         del i
# print(n)

# n = [20, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n.insert(0, 20)
# print(n)

# n.remove(20)
# print(n)

# print(n.index(4))

# x = 0
# while x < 10:
#     x = x + 1
#     if x < 3:
#         continue
#     print(x)
#     if x > 7:
#         break

# x = 4
# print(x < 3)
# print(x > 3)

# x = 1
# total = 0
# while 1:
#     total = total + x
#     if total > 10:
#         print(x)
#         print(total)
#         break
#     x = x + 1


# inData = int(input())

# i = 2
# line = 0


# 13
# 2~13

# while i <= inData:
#     j = 2
#     while j <= i:
#         if 13 % 13 == 0:
#             break
#         j += 1

#     print(f"i : {i}, j : {j}")
#     if i == j:
#         print(i)
#         line += 1
#         if(line == 7):
#             line = 0
#             print()
#     i += 1


a = [3, 5, 1, 55, 7, 10]

print(a)
print()

for i in range(len(a)):
    value = a.pop(0)
    a.append(value)
    print(a)
