# 복습시작
# 딕셔너리를 이용한 계산기 만들기

# s = int(input("첫번째 숫자"))
# s1 = int(input("두번째 숫자"))
# user = input("연산자")
# num = {"+":s+s1 , "-":s-s1 , "*":s*s1 , "/":s/s1}
# if user not in num:
#     print('잘못된 연산자입니다')
# elif (user == '/' and s1 == 0):
#     print("0으로 나눌 수 없습니다")
# else:
#     print(num[user],"입니다")
# 왜! 이게!!! elif 조건이 안되는데!!!!왜1!!!!!

# for i in reversed(range(0, 10)):
#     print("love you", i)

# s = int(input("시작"))
# e = int(input("끝"))
# g = int(input("간격"))
# if g < 0:
#     e = e - 1
# else:
#     e = e + 1
# for i in range(s,e,g):
#     print(i)
# if조건이 안됨

# s = int(input("시작"))
# e = int(input("끝"))
# g = int(input("간격"))
# for i in range(s,e+1,g):
#     print("love", i)

# for i in 'python':
#     print(i, end = ' ')

# a = [49, -17, 25, 102, 8, 62, 21]
# for i in a:
#     print(i * 10, end = ' ')

# a = int(input("숫자"))
# for i in range(1, 10):
#     print(a, "*", i, "=", a*i)

# t = 0 
# user = int(input("총합을 구할 숫자 입력: "))
# for i in range(user):
#     t = t + i
# print(t)

s = int(input("숫자"))
t = 0
while s > 0:
    t += s
    s -= 1
print(t)