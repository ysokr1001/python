# r = range(6,10)
# # print(list(r))
# print(list(r[::2]))
# # print(r[:7:2])

#복습
# coin = int(input("금액을 넣어주세요"))
# if coin > 10000:
#     print("금액을 초과했습니다")
# elif coin <= 0:
#     print("0원입니다")
# else:
#     drink = int(input("음료 선택: 1 사이다, 2 콜라, 3오렌지쥬스"))
#     if drink == 1:
#         if coin < 700:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은",coin-700, "입니다")
#     elif drink == 2:
#         if coin < 600:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은",coin-600, "입니다")
#     elif drink == 3:
#         if coin < 800:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은",coin-800, "입니다")
#     else:
#         print("다시 음료를 선택해주세요")

# Coin = int(input("금액을 넣어주세요:"))
# drink = {"사이다" : 700, "콜라":600, "오렌지쥬스":800}
# if Coin > 10000:
#     print("") 
# else:
#     user = str(input("사이다, 콜라, 오렌지쥬스"))
#     if Coin - drink[user]<0:
#         print("잔액이 부족합니다")
#     else:
#         re = Coin - drink[user]
#         print("잔액은" , re , "입니다")

# coin = int(input("금액을 넣어주세요"))
# d = {'사이다':700, '콜라':600, '오렌지쥬스':800}
# if coin > 10000:
#     print("금액을 초과했습니다")
# elif coin <= 0:
#     print("0원입니다")
# else:
#     d2 = str(input("음료를 선택하세요 : 사이다, 콜라, 오렌지쥬스"))
#     if d2 in d:
#         if coin - d[d2] <0:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은",coin-d[d2], "입니다")
#     else:
#         print("다시 음료를 선택해주세요")
#복습해보기

# z = ["+", "-", "*", "/"]
# s = int(input("첫번째 숫자"))
# s1 = int(input("두번째 숫자"))
# user = input("연산자를 선택하세요")
# if user in z:
#     if user == "+":
#         print(s+s1, "입니다")
#     elif user == "-":
#         print(s-s1, "입니다")
#     elif user == "*":
#         print(s*s1, "입니다")
#     elif user == "/":
#         if s1 != 0:
#             print(s/s1, "입니다")
#         else:
#             print("0으로 나눌 수 없습니다")
# else:
#     print("잘못된 연산자입니다")

# s = int(input("첫번째 숫자"))
# s1 = int(input("두번째 숫자"))
# user = input("연산자를 입력하세요")
# d = {"+":s+s1 , "-":s-s1 , "*":s*s1 , "/":s/s1}
# if user not in d:
#     print("잘못된 연산자 입니다")
# elif (s1==0 and user == "/"):
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(d[user],"입니다")
#0으로 나눌 수 없습니다....?ㅠㅠㅠ

# s = int(input("첫번째"))
# s1 = int(input("두번째"))
# user = input("연산자")
# user_list = ["+", "-", "*", "/"]
# if user not in user_list:
#     print("잘못된 연산자입니다")
# elif s1 == 0 and user == "/":
#     print("0으로 나눌 수 없습니다")
# else:
#     answer = dict(zip(user_list,[s+s1, s-s1, s*s1, s/s1]))
#     print(answer[user], "입니다")
#다시다시다시다시ㅏ디사디사;

# for z in range(5, 12):
#     print('hello!', z)

# for z in range(0, 9, 2):
# print('hello!', z)

# for z in range(10, 0):
#     print('hello!', z)

# for z in range(10, -1, -1):
#     print('hello!', z)

# s = int(input("시작숫자"))
# e = int(input("끝숫자"))
# i = int(input("간격"))
# for z in (range(s,e,i)):
#     print(z)

#감소하게? 0보다 작을 때 출력이 안됨
# s = int(input("시작숫자"))
# e = int(input("끝숫자"))
# i = int(input("간격"))
# if i < 0:
#     e = e - 1
# else:
#     e = e + 1
# for z in (range(s,e,i)):
#     print(z)

# a = [10, 20, 30, 40, 50]
# for i in a:
#     print(i)

# fruits = ('apple', 'banana', 'grape')
# for fruit in fruits:
#     print(fruit)

# for letter in reversed('python'):
#     print(letter, end=' ')

# x = [49, -17, 25, 102, 7, 62, 21]
# for i in x:
#     print(i*10, end = " ")
#이거 잘 안됨 ?!?! ㅠ_ㅠ

# user = int(input("입력"))
# for i in range(10):
#     print(user, "*" , i ,"=" , user*i)

# user = int(input("입력한 값까지의 합을 구합니다"))
# for i in range(user):
#     t = range(user) + i
#     print(t)

# 어려워요오오오옹 t=0 입력안하면 출력이 안되는균 ㅠ_ㅠ 
# t = 0
# user = int(input("입력한 값까지의 합을 구합니다"))
# for i in range(user+1):
#     t = t + i
# print(t)

# 만약 1부터 10까지의 숫자가 hello에 찍히게 하고 싶다면?
# i = 1
# while i < 10:
#     print('Hello', i)
#     i += 1 #i = i+1 축약

# i = 100
# while i > 0:
#     print('Hello', i)
#     i -= 1 

# i = 1
# while i <= 10:
#     print('Hello', i)
#     i += 1
# c = int(input("반복할 횟수"))
# while 0 < reversed(range(c)):
#     print('hello', c)
#     c -= 1
# c = int(input("반복할 횟수"))
# while 0 < c:
#     print('hello', c)
#     c -= 1

# t = 0
# user = int(input("입력한 값까지의 총합 구하기"))
# for i in range(user):
#     t = t + i
# print(t)

# t = 0
# c = int(input("입력한 값까지의 총합 구하기"))
# while 0 < c:
#     print(t)
#     t = t + range(c)

#이해를 해야한다..... !!! 
# t = 0
# n = int(input("입력한 값까지의 총합 구하기"))
# while 0 < n:
#     t += n
#     n -= 1
# print(t)
