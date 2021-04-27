# for 반복문을 이용한 정수 출력
# a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)

# 위를 map사용해서 출력해보기
# a = [1.2, 2.5, 3.7, 4.6]
# print(list(map(int, a)))

# 리스트에 있는 걸 문자열로
# a = list(map(str, range(1, 10)))
# print(a)

# for문으로 요소 출력
# a = [1, 3, 5, 7]
# for i in a:
#     print(i, end=" ")

# while문으로 요소 출력
# i = 1
# while i < len(a):
#     print(a[i], end=" ")
#     i += 1

# 리스트 튜플 응용 문자열 길이가 5이상인거 찾기
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']
# b = [i for i in a if len(a) > 5]
# print(b)

# 리스트 튜플 응용2 표준입력으로 숫자2개를 입력받아서 2의 거듭제곱근 출력
# s = int(input("첫번째 숫자"))
# s1 = int(input("두번째 숫자"))
# two = []

# for i in range(s, s1+1):
#     z = 2 ** i
#     two.append(z)
# del two[1]
# del two[-2]
# print(two, end=' ')

# 랜덤 함수를 사용해서 로또숫자 7자리 10번씩 받기 대신 중복이 되면 안됨
# import random

# for i in range(10):
#     number = []
#     while len(number) < 7:
#         ran = random.randint(1, 50)
#         if ran not in number:
#             number.append(ran)
#     print(number)

# 간단 버전으로
# import random

# for i in range(10):
#     z = random.sample(range(1, 51), 7)
#     print(z)

# 2차원리스트
# a = [[10, 20], [30, 40], [50, 60]]
# for i in range(len(a)):
#     i = a[i]
#     print(i)

# 위 a요소 출력
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# while문 한번으로 요소 출력

# i = 0
# while i < len(a):
#     x, y = a[i]
#     print(x, y)
#     i += 1

# for문과 while문을 사용해서 다음의 요소를 출력

# a = [[1, 2, 3], [5, 6, 7], [8, 9, 10], [12, 13, 14]]

# for i in range(len(a)):
#     j = 0
#     while j < len(a[i]):
#         print(a[i][j], end=' ')
#         j += 1
#     print()

# for 반복문으로 2차원리스트 만들기
