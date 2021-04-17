# count = int(input("반복횟수"))
# count_back= count +1
# while count>0:
#     print("love", count_back - count)
#     count -= 1
# TODO 다시 한번 짜보면서 이해하기

# import random
# print(random.random())
# print(random.random())

# import random
# import inspect
# print(inspect.getfile(random))

# import random
# i = 0
# while i < 10:
#     print(random.random(), i)
#     i = i + 1

# 주사위를 만들어보자규 10번반복!
# import random
# i = 0
# while i < 10:
#     print(random.randint(1,6))
#     i = i + 1

# cnt_rand = [0, 0, 0, 0, 0, 0]
# import random
# i = 0
# while i < 10:
#     r = random.randint(1,6)
#     if cnt_rand[1] == r:
#         if r == 1:
#             print(cnt_rand[0])
#     i = i + 1
# if cnt_rand[0] == r:
#     if r == 1:
#         print(cnt_rand[1])

# import random
# i = 0
# while i < 10:
#     r = random.randint(1,6)
#     cnt_rand = [0, 0, 0, 0, 0, 0]
#     if r == 1:
#        print(cnt_rand[0] ,"=" ,r+1,)
#     i = i + 1
# print(cnt_rand,)

# import random
# i = 0
# cnt_rand = [0, 0, 0, 0, 0, 0]
# while i < 10:
#     r = random.randint(1,6)
#     print(r)
#     cnt_rand[r-1] =cnt_rand[r-1] +1
#     i = i + 1
# print(cnt_rand)
# TODO 일단 이해만 해도 좋다고 하심
# TODO 근데 58번째 줄은 왜..? 굳이...? 계산 돌려봐도 cnt자리에 들어가나?

# 3이 나오면 종료
# import random
# i = 0
# while i < 10:
#     r = random.randint(1,6)
#     print(r)

# TODO 왜 나는 무한으로 도는 것인가..?
# import random
# i = 0
# while i != 3:
#     r = random.randint(1,6)
#     print(r)

# 아싸룽 혼자 풀오따요
# i = 2
# j = 5
# while i < 33 or j < 0 :
#     print(i, j)
#     i *= 2
#     j -= 1

# m = int(input("교통카드 충전액을 입력하세요:"))
# i = 1,350
# while 1350 < m:
#     print("잔액은" ,m-i,"입니다")
#     i = m - i

# 정답
# m = int(input("교통카드 충전액을 입력하세요:"))
# while 1350 <= m:
#     m = m -1350
#     print(m)

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 100:
#         break

# t = i
# while True:
#     print(t)
# 0-100까지 총합구하기 아예 못풀었음 TODO

# i = 0
# t = 0
# while True:
#     i = i + 1
#     t = t + i
#     print(i)
#     if i == 100:
#         break
# print(t)

# for break
# for i in range(100):
#     print(i)
#     if i == 10:
#         break

# i = 0
# t = 0
# for i in range(1000):
#     i = i + 1
#     t = t + i
#     print(t)
#     if i == 100:
#         break
# TODO 다시 짜보기 복잡하게 짬 답보면서

# t = 0
# for i in range(1000):
#     t = t + i
#     if i == 100:
#         break
# print(t)

# 짝수 2== 0, 홀수 2==1 이구나!
# for i in range(100):
#     if i % 2 == 1 :
#         continue
#     print(i, end = " ")

# # while 짝수 건너뛰기
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# 숫자 입력받아 반복하기 While
# c = int(input("반복숫자 입력"))
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == c:
#         break

# TODO 잘못된 부분 찾아보기
# ck = int(input("숫자를 입력하세요:"))
# for i in ck:
#     if i % 2 == 0 :
#         continue
#     print(i, end = " ")

# ck = int(input("숫자를 입력하세요:"))
# for i in range(ck):
#     if i % 2 == 0 :
#         continue
#     print(i, end = " ")

#  이식이 왜 성립이 안되나? TODO
# i = 0
# while True:
#     if i[:1] or i[0] == 3:
#         continue
#     else:
#         break
#     print(i)
#     i += 1

# i = 0
# while True:
#     if i < 74:
#         i % == 3
#         continue
#     if i != 3:
#         break
#     print(i, end=" ")
#     i += 1

# TODO 왜? i += 1을 해주는거지? 오히려 3일때여야 하는거 아닌가? 202번줄
# i = 0
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue
#     if i>73:
#         break
#     print(i, end=" ")
#     i += 1

# start, stop = map(int, input().split())
# i = start
# while True:
#     if map(int(start 200 and start > 1), int(stop>10 and stop<200)

# start, stop = map(int, input().split())
# i = start
# while True:
#     if (i % 10 == 3):
#         i += 1
#         continue
#     if (i>stop):
#         break
#     print(i, end=" ")
#     i += 1

# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep ='', end= '')
#     print(' i:', i,'//n', sep=' ')
# j:0j:1j:2j:3j:4 i: 0 //n
# j:0j:1j:2j:3j:4 i: 1 //n
# j:0j:1j:2j:3j:4 i: 2 //n
# j:0j:1j:2j:3j:4 i: 3 //n
# j:0j:1j:2j:3j:4 i: 4 //n

# i = 0
# j = 0
# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep ='', end= '')
#     print(' i:', i, sep=' ')

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j == '*':
#             print('*', end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print('*', end='')
#     print()


# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         else:
#             print(j, sep=' ')

# 다른 사람이 푼 답
# for i in range(5):
#     for j in range(5):
#         if j < i:
#             print(' ', end='')
#     print("*")

# i = 0
# for i in range(5):
#     print(i*range(5),)

# for i in range(5):
#     print('*' * (i+1))

#과제 -첫번째시도
# for i in range(4):
#     # for j in range(4):
#     #     if j == i+1:
#     #         print(' ', end = '')
#     for z in range(9):
#         if z % 2 == 1:
#             print("*", end = ' ')
#     print('*')

# 별이 한개씩 증가하는 코드
# for i in range(5):
#     for j in range(i+1):
#             print('*', end='')
#     print()

# 별이 공백 한칸씩 두며 한개씩 출력하는 코드
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         else:
#             print(' ', end=' ')
#     print()

# 과제 두번째시도
# for i in range(4):
#     for j in range(7):
#         if j <= (i):
#             print('*', end = '')
#     for z in range(i):
#             print(' ', end = ' ')
#     print()

# 과제 간단식 완료
# 수정해줌
# for i in range(5):
#     for j in range(i*(-1)+5):
#         print(' ', end="")
#     for z in range(i*2+1):
#         print('*', end="")
#     print(end='\n')


# i = range(5)
# for z in i:
#     print('*' * (z*2+1))

# for i in range(5):
#     for j in range(1):
#         print(' '*(i*(-1)+5), end = '')
#     for z in range(1):
#         print('*' * (i*2+1))
# print( )

# 과제 제출 1
# for i in range(5):
#     print('-'*(i*-1+5)+'*' * (i*2+1))

# 과제 제출 2
for i in range(5):
    for j in range(i*(-1)+5):
        print(' ', end='')
    for z in range((i*2+1)):
        print('*', end="")
    print()
