# for i in range(5):
#     print(' '*(i*-1+5)+'*' * (i*2+1))

# x = 4
# for i in range(1, x+1):
#     print(' '*(x-i) + '*'*(2*i-1))

# for i in range(5):
#     print(' '*(i+1) + '*'*(i*-1+5))

# for i in range(5):
#     for j in range(5):
#         if j < i:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# user = int(input("출력숫자"))
# for i in range(user):
#     for j in range(i*(-1)+5):
#         print(' ', end='')
#     for z in range((i*2+1)):
#         print('*', end="")
#     print()

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

# for i in range(1, 101):
#     FizzBuzz = i % 5 == 0 and i % 3 == 0
#     Fizz = i % 3 == 0
#     Buzz = i % 5 == 0
#     print(i, +, FizzBuzz, +, Fizz, +, Buzz)

# or이 처리가 안돼서 처리가 안됐었음 거의 다 왔다! ㅎㅎ
# for i in range(1, 101):
#     print('FizzBuzz'*(i % 5 == 0 and i % 3 == 0) +
#           'Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or i)

# for i in range(1, 101):
#     print('Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or i)

# 2와 11의 배수, 공배수
# for i in range(1, 101):
#     if i % 2 == 0 and i % 11 == 0:
#         print('FizzBuzz')
#     elif i % 2 == 0:
#         print('Fizz')
#     elif i % 11 == 0:
#         print('Buzz')
#     else:
#         print(i)
# import turtle as t
# t.shape('turtle')
# t.forward(100)

# import turtle as t
# t.shape('turtle')

# 반복문 예제1 - 다시 안보고 짜보기
# t = 0
# start = int(input("시작"))
# stop = int(input("끝자리"))
# for i in range(start, stop+1):
#     t = t + i
# print("총합은", t, "입니다")

# 미완료
# start = int(input("시작"))
# stop = int(input("끝자리"))
# t = 0
# for i in range(start, stop+1):
#     if i % 2 == 0:
#         z = i**2
#         print(z)
#         t = t+z
# print("총합은", t, "입니다")

# test = int(input("테스트"))
# test1 = int(input("테스트1"))
# test2 = int(input("테스트2"))
# test3 = int(input("테스트3"))
# test4 = int(input("테스트4"))
# Scores = list('test', 'test1', 'test2', 'test3', 'test4')
# print(Scores)

# Scores = [70, 50, 85, 98, 82]
# user = list(map(int, input().split()))
# m = max(user)
# n = min(user)
# sum = 0
# t = 0
# e = 0
# for i in user:
#     sum += i
#     t = sum - m - n
#     e = t/3
# print(e)

# n = Scores[0]
# for i in Scores:
#     if i < n:
#         n = i
# print(n)

# user = list(map(int, input().split()))
# m = user[0]
# n = user[0]
# sum = 0
# t = 0
# e = 0
# for i in user:
#     if i < n:
#         n = i
#     elif i > m:
#         m = i
#     sum += i
#     t = sum - m - n
#     e = t/3
# print(e)

# print(n)
# print(m)
# print(t)
# m = Scores[0]
# for i in range(1, len(Scores)):
#     if m < Scores[i]:
#         m = Scores[i]
# print(m)

# user = list(map(int, input().split()))
# sum = 0
# t = 0
# e = 0
# for i in user:
#     sum += i
#     t = sum - m - n
#     e = t/3
# print(e)
# print(m)

scores = list(map(int, input().split()))
max = scores[0]
min = scores[0]
sum = 0
total = 0
average = 0
for i in scores:
    sum += i
    if i < min:
        min = i
    elif i > max:
        max = i
total = sum - max - min
average = total/3
print(average)
