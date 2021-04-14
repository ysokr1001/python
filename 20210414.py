
# user = int(input("값입력"))
# number = user + 20 # 275
# if(number > 255 ):
#     number = 255

# print("출력값 : ", number)
# if (0 <= user <= 255):
#     print(user+20)
# elif (user>255):
#     print(255)
# else:
#     print("0~255사이로 입력하세요 ")

# user = int(input("값입력"))
# if user - 20 <= 255:
#     print(user-20)
# elif user - 20 > 0:
#     print("0")
# else:
#     print("다시 입력하세요")
#대성이한테 물어보기 if조건문예제

# user = int(input("값입력"))
# if 0 < user -20 :
#    print(user-20)
# elif user-20 > 255:
#     print("255이상")
# else:
#     print("0")
# 대성이한테 물어보기 초과한 값이 그대로 출력됨

# age = str(input("나이를 입력하세요"))
# if '0세'<= age and age <= '19세':
#     print("미성년자입니다")
# elif '20세'<=age and age<= '99세':
#     print("성인입니다")
# else:
#     age = age > '100세'
#     print("다시입력해주세요", age)

#예제2복습
# user = int(input("숫자를 입력하세요"))
# if user + 20 > 255:
#     print("255이상입니다")
# elif user + 20 > 0:
#     print(user+20)
# else:
#     print("다시 입력하세요")
#답하고 비교해서 둥둥이한테 물어보기 정답은 출력됨

# c = input("현재시간:")
# if c[3:] == '00':
#     print ("정각입니다")
# else:
#     print ("정각이 아닙니다")

# fruit = ["사과", "포도", "홍시"]
# user = str(input("과일을 입력하세요"))
# if user in fruit:
#     print(user, "입니다")
# else:
#     print("오답입니다")

# t = ["Microsoft", "google", "Naver", "Kakao", "SANSUNG", "LG"]
# user = str(input("종목을 입력하세요"))
# if user in t:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다")

# F = {"봄" : "딸기", "여름": "토마토", "가을": "사과"}
# user = str(input("좋아하는 계절은?"))
# if user in F:
#     print(user, "입니다")
# else:
#     print("오답입니다")

# F = {"봄" : "딸기", "여름": "토마토", "가을": "사과"}
# user = str(input("좋아하는 과일은?"))
# if user in F.values():
#     print(user, "입니다")
# else:
#     print("오답입니다")

# Coin = int(input("금액을 넣어주세요:"))
# drink = int(input("음료선택: 1 사이다, 2 콜라, 3 오렌지쥬스"))
# if Coin <= 600:
#     print("금액이부족합니다")
# elif Coin <= 10000:
#     print(Coin,"을 넣어주셨습니다") 
#     if drink == 1:
#         if(Coin - 700 < 0 ): 
#             print("금액이부족합니다")
#         else:
#             print("잔액은" ,Coin-700, "입니다")
#     elif drink == 2:
#         print("잔액은" ,Coin - 600, "입니다")
#     elif drink == 3:
#         print("잔액은" ,Coin - 800, "입니다")
#     else:
#         print("다시 선택해주세요")
# else:
#     print("최대금액이 초과되었습니다")


# Coin = int(input("금액을 넣어주세요:"))
# if Coin > 10000:
#     print("초과했습니다")
# elif Coin < 0:
#     print("0원 미만입니다")
# else:
#     drink = int(input("음료선택: 1 사이다, 2 콜라, 3 오렌지쥬스"))
#     if drink == 1:
#         if Coin < 700:
#             print("잔액이부족합니다")
#         else:
#             print(Coin-700,"원입니다")
#     elif drink == 2:
#         if Coin < 800:
#             print("잔액이부족합니다")
#         else:
#             print(Coin-800,"원입니다")


# coin = int(input("금액을 넣어주세요"))
# if coin >10000:
#     print("금액을 초과했습니다")
# elif coin <0:
#     print("0원입니다")
# else:
#     d = int(input("음료선택: 1 식혜, 2 수정과"))
#     if d == 1:
#         if coin < 500:
#             print("잔액이 부족합니다")
#         else:
#             print(coin-500, "입니다")
#     elif d == 2:
#         if coin <600:
#             print("잔액이 부족합니다")
#         else:
#             print(coin-700, "입니다")



# F = {"봄" : "딸기", "여름": "토마토", "가을": "사과"}
# user = str(input("좋아하는 과일은?"))
# if user in F.values():
#     print(user, "입니다")
# else:
#     print("오답입니다")

# Coin = int(input("금액을 넣어주세요:"))
# drink = int(input("음료선택: 1 사이다, 2 콜라, 3 오렌지쥬스"))
# if Coin <= 10000:
#     print(Coin,"을 넣어주셨습니다") 
#     if drink == 1:
#         if Coin <= 500:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은" ,Coin-700, "입니다")
#     elif drink == 2:
#         if Coin <= 600:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은" ,Coin-700, "입니다")
#     elif drink == 3:
#         if Coin <= 700:
#             print("잔액이 부족합니다")
#         else:
#             print("잔액은" ,Coin-800, "입니다")
# else:
#     print("금액을 다시 넣어주세요")

# Coin = int(input("금액을 넣어주세요:"))
# user = str(input("사이다, 콜라, 오렌지쥬스"))
# drink = {"사이다" : 700, "콜라":600, "오렌지쥬스":800}
# if Coin <= 10000:
#     print(Coin,"을 넣어주셨습니다") 
#     if user in drink:
#         if Coin <= drink.values():
#             print("잔액이 부족합니다")
#     else:
#          print("잔액은" , Coin - drink.values() , "입니다")
#     # elif user in drink:
#     #     if Coin <= 600:
#     #         print("잔액이 부족합니다")
#     #     else:
#     #         print("잔액은" ,Coin-drink.values(), "입니다")
#     # elif user in drink:
#     #     if Coin <= 700:
#     #         print("잔액이 부족합니다")
#     #     else:
#     #         print("잔액은" ,Coin-drink.values(), "입니다")
# else:
#     print("금액을 다시 넣어주세요")

Coin = int(input("금액을 넣어주세요:"))
drink = {"사이다" : 700, "콜라":600, "오렌지쥬스":800}
if Coin > 10000:
    print("") 
else:
    user = str(input("사이다, 콜라, 오렌지쥬스"))
    if Coin - drink[user]<0:
        print("잔액이 부족합니다")
    else:
        re = Coin - drink[user]
        print("잔액은" , re , "입니다")

# z = ["+", "-", "*", "/", "="]
# s = int(input("첫번째 숫자를 입력하세요"))
# s1 = int(input("두번째 숫자를 입력하세요"))
# user = input("연산자를 선택하세요")
# if user in "+":
#     print(s + s1)
# elif z == "-":
#     print(s - s1)
# elif z == "*":
#     print(s * s1)
# elif z == "/":
#     print(s / s1)
# # else:
# #     print((s/s1)= 0, "다시 계산해주세요")

# s = int(input("첫번째 숫자를 입력하세요"))
# s1 = int(input("두번째 숫자를 입력하세요"))
# user = input("연산자를 선택하세요")
# if user == "+":
#     print(s + s1)
# elif user == "-":
#     print(s - s1)
# elif user == "*":
#     print(s * s1)
# elif user == "/":
#     if s1 != 0:
#         print(s / s1)
#     else:
#         print("0으로 나눌 수 없습니다")
# else:
#     print("잘못된 연산자")

