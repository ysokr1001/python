# x = int(input("숫자입력"))
# if x != 10:
#     print("OK")
# elif x == 15:
#     print("15입니다")
# elif x == 20:
#     print("20입니다")
# else:
#     print("다시 입력하세요")

# coin = int(input("가격을 입력하세요"))
# coupon = input("쿠폰 입력: cash3000, cash5000")

# if coupon == 'cash3000':
#     print("지불금액은:", coin-3000, "입니다")
# elif coupon == 'cash5000':
#     print("지불금액은:", coin-5000, "입니다")
# else:
#     print("쿠폰을 다시 입력해주세요")

# 짝수홀수출력
# user = int(input("숫자입력"))
# if user % 2 == 0:
#     print("짝수입니다")
# if user % 2 == 1:
#     print("홀수입니다")

# test = int(input("점수를 입력하세요"))
# co = input("통과여부: True, False")

# if test >= 80 and co == 'True':
#     print("합격입니다")
# else:
#     print("불합격입니다")

# kor = int(input("점수를 입력하세요"))
# eng = int(input("점수를 입력하세요"))

# if kor >= 90 and eng >= 70:
#     print("합격입니다")
# else:
#     print("불합격입니다")

# 과목은 0과 100사이, 평균점수 80점 이상이어야만 합격
# kor = int(input("점수를 입력하세요"))
# eng = int(input("점수를 입력하세요"))

# if (0 < kor < 100 and 0 < eng < 100):
#     total = (kor + eng) / 2
#     if total >= 80:
#         print("합격입니다")
#     else:
#         print("불합격입니다")
# else:
#     print("점수는 0과 100사이로 입력해주세요")

# 음료수 자판기 만들기 1
# button = int(input("1: 콜라, 2:사이다, 3:환타"))
# if button == 1:
#     print("콜라입니다")
# elif button == 2:
#     print("사이다 입니다")
# elif button == 3:
#     print("환타입니다")
# else:
#     print("다시 눌러주세요")

# 학생인가 아닌가, 학생이라면 어떤 학생인가?

# user = int(input("1: 학생, 2: 학생아님"))

# if user == 1:
#     print("학생이며")
#     stu = input("초등학생, 중학생, 고등학생")
#     if stu == "초등학생":
#         print("초등학생입니다")
#     elif stu == "중학생":
#         print("중학생입니다")
#     elif stu == "고등학생":
#         print("고등학생입니다")
#     else:
#         print("대학생 이상입니다")
# else:
#     print("성인입니다")

# 음료수자판기 2

# money = int(input("금액을 넣어주세요"))
# button = int(input("1:콜라 600원, 2:사이다 700원, 3: 식혜 500원"))

# if button == 1:
#     print("잔액은", money - 600)
# elif button == 2:
#     print("잔액은", money - 700)
# elif button == 3:
#     print("잔액은", money - 500)
# else:
#     print("다시 선택해주세요")

# 교통카드
# age = int(input("나이입력"))
# balance = 9000

# if 7 <= age <= 12:
#     print("잔액은", balance-650, "입니다")
# elif 13 <= age <= 18:
#     print("잔액은", balance-1050, "입니다")
# elif 19 <= age:
#     print("잔액은", balance-1250, "입니다")
# else:
#     balance = balance
#     print(balance)

# 값을 입력받고 +20, 0~255사이
# user = int(input("값을 입력하세요"))

# if 0 <= user + 20 <= 255:
#     print(user + 20,)
# else:
#     user + 20 > 255
#     print("255이상입니다")

# 미성년자인지 판단하시오
# user = input("나이를 입력하세요:")

# if '10세' <= user and user <= '99세':
#     if user <= '19세':
#         print("미성년입니다")
#     else:
#         print("성년입니다")
# else:
#     print("10-99세 사이로 입력해주세요")

# 입력받은 시간이 정각인지 아닌지 판별하시오
# clock = input("00:00으로 현재 시간을 입력하세요")

# if clock[3:] == '00':
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

# 투자경고종목인가 아닌가?
# warn = ["microsoft", 'google', 'naver', 'kakao', 'sansung', 'lg']
# user = input("투자 종목을 입력하세요")

# if user in warn:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다")

# 딕셔너리 값 안에 포함되어 있다면 정답
# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# user = input("계절을 입력하세요")
# if user in fruit:
#     print("정답")
# else:
#     print("오답")

# 자판기만들기 3
# coin = int(input("금액입력"))

# if coin <= 0:
#     print("금액을 넣어주세요")
# elif coin > 10000:
#     print("금액이 초과하였습니다")
# else:
#     button = int(input("1번 사이다 700원, 2번 콜라 600원, 3번 오렌지쥬스 800원"))
#     if button == 1:
#         if coin < 700:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은", coin-700)
#     elif button == 2:
#         if coin < 600:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은", coin-600)
#     elif button == 3:
#         if coin < 800:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은", coin-800)
#     else:
#         print("버튼을 다시 눌러주세요")

# text 계산기 만들기
# z = ['+', '-', '/', '*']
# user = input("연산자를 선택하세요")

# if user in z:
#     i = int(input("첫번째 숫자"))
#     j = int(input("두번째 숫자"))
#     if user == '+':
#         print(i + j, "입니다")
#     elif user == '-':
#         print(i-j, "입니다")
#     elif user == '*':
#         print(i*j, "입니다")
#     elif user == '/':
#         if j == 0:
#             print("0으로 나눌 수 없습니다")
#         else:
#             print(i/j, "입니다")
#     else:
#         print("뭐지 도대체 뭘 누른거야 넌")
# else:
#     print("연산자를 다시 선택해주세요")

# 딕셔너리 계산기
# s1 = int(input("첫번째 숫자"))
# s2 = int(input("두번째 숫자"))
# user = input("연산자를 선택하세요")
# if (user == '/' and s2 == 0):
#     print("0으로 나눌 수 없습니다")
# else:
#     z = {'+': s1+s2, '-': s1-s2, '*': s1*s2, "/": s1/s2}

#     if user in z:
#         print(z[user], "입니다")
#     else:
#         print("잘못된 연산자입니다")

# 숫자를 입력받아 증감 방향 설정하기

# start = int(input("시작숫자"))
# stop = int(input("끝숫자"))
# z = int(input("거리"))
# for i in range(start, stop+1, z):
#     print(i)

# x = [49, -17, 25, 102, 8, 62, 21]
# for i in x:
#     print(i*10, end=' ')

# 총합구하기
# t = 0
# user = int(input("총합을 구할 숫자를 입력하세요"))

# for i in range(user):
#     t += i
# print("총합은", t, "입니다")

# while 입력받은 수만큼 더하기
# user = int(input("총합구하기"))
# i = 0
# t = 0
# while i < user + 1:
#     t += i
#     i += 1
# print("총합은:", t)

# while문을 사용하여 1~6까지의 정수형 random
# import random

# count = [0, 0, 0, 0, 0, 0]
# i = 0
# while i < 10:
#     ran = random.randint(1, 6)
#     print(ran)
#     count[ran-1] = count[ran-1] + 1
#     i += 1
# print(count)

# 위의 while문 반복하다가 3이 나오면 끊기
# import random

# i = 0
# while i != 3:
#     i = random.randint(1, 6)
#     print(i)

# 두줄 출력
# i = 2
# j = 5

# while i <= 32 or j >= 1:
#     print(i, j)
#     i *= 2
#     j -= 1
