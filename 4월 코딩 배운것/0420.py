# test = int(input("점수를 입력하세요"))
# # count[0, 0, 0, 0, 0]
# grade_counter[0, 0, 0, 0, 0]
# # for i in count[]:
# if 85 <= test and test < 100:
#     grade_counter[0] == grade_counter(count+1)
# elif 70 <= test and test <= 84:
#     grade_gounter['b'] == [1]
# elif 55 <= test and test <= 69:
#     grade_counter['c'] == [2]
# elif 40 <= test and test <= 54:
#     grade_counter['d'] == [3]
# elif 0 <= test and test <= 39:
#     grade_counter['e'] == [4]
# else:
#     print("점수를 다시 입력하세요")

# 안돌아감
test = (input("점수를 입력하세요").split(" "))
# print(test)

# test = list(map(int, input("점수를 입력하세요").split(" ")))
# print(test)
grade_counter = [0, 0, 0, 0, 0]
for i in test:
    if 85 <= i and i < 100:
        grade_counter[0] += 1
    elif 70 <= i and i <= 84:
        grade_counter[1] += 1
    elif 55 <= i and i <= 69:
        grade_counter[2] += 1
    elif 40 <= i and i <= 54:
        grade_counter[3] += 1
    elif 0 <= i and i <= 39:
        grade_counter[4] += 1
    else:
        print("점수를 다시 입력하세요")
print(grade_counter)

# name_list = ['matthew', 'mark', 'luke', 'john', 'paul', 'peter']
# count = [0]
# for i in name_list:
#     if 'm' in i or 'n' in i:
#         count[0] += 1
#     # elif 'n' in i:
#     #     count[0] += 1
# print(count)

# marks = [90, 25, 67, 45, 80]
# j = 0
# for i in marks:
#     j = j+1
#     if i > 60:
#         print(j, "합격을 축하드립니다")
#     elif i <= 60:
#         print()

# i = 0
# while i > marks:
#     print("합격입니다")

# marks = [90, 25, 67, 45, 80]
# j = 0
# for i in marks:
#     j = j+1
#     if i > 60:
#         print("%d번 학생 합격을 축하드립니다" % j)
#     elif i <= 60:
#         print()

# marks = [90, 25, 67, 45, 80]
# number = 0

# i = 0
# while marks[0]:
#     if marks > 60:
#         number = number+1
#         continue
#     if marks < 60:
#         break
#     print("%d번 학생 합격을 축하드립니다" % number)

# marks = [90, 25, 67, 45, 80]
# i = 0
# while i < len(marks):
#     i += 1
#     if marks[i - 1] < 60:
#         continue
#     print(i, "번 학생 축하합니다. 합격입니다.")

# arr = [1, 4, 2, 3]

# left, right = 0, len(arr)-1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print("변환된 arr은", arr, "입니다")
# left, right = 0, len(arr)-1
# arr[left], arr[right] = arr[right], arr[left]:
#     left += 1
#     right -= 1
# print(arr)

# gugu = int(input("첫번째 숫자"))
# for i in range(1, 9):
#     print(gugu, 'X', i, '=', gugu*i)

# gugu = int(input("첫번째 숫자"))
# i = 0
# while i < 10:
#     print(gugu, 'X', i, '=', gugu*i)
#     i += 1

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i, 'X', j, '=', i*j)

# i = 2
# while i < 10:
#     for j in range(1, 10):
#         print(i, 'X', j, '=', i*j)
#     i += 1


# for i in range(1, 10):
#     for j in range(2, 10):
#         # print(j, 'X', i, '=', j*i, sep='', end='\t')
#         print(f"{j}x{i}={j*i}", sep='', end='\t')
#     print()

# i = 2
# j = 1
# while i < 10:
#     while j < 10:
#         print(i, 'X', j, '=', i*j, sep='', end='  ')
#         j += 1
#         i += 1
# print()

# i = 1
# j = 2
# while i < 10:
#     while j < 10:
#         print(j, 'X', i, '=', j*i, sep='', end='  ')
#         j += 1
#     i += 1
#     j = 2
#     print()


# votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
# candidates = [0, "전정국", "김남준", "박지민", "정호석", "김태형"]
# count = [0, 0, 0, 0, 0, 0]
# for i in votes:
#     count[i] += 1
# print(count)

# lar = 0  # 최대 득표수
# idx = 0  # 최대 득표한 사람의 번호
# for i, val in enumerate(count):
#     if val > lar:
#         lar = val
#         idx = i
# print(lar)

# result = candidates[idx]
# print(result, "후보가", lar, "표로 당선이 확정되었습니다")

# import random
# li = []
# user = int(input("숫자 입력"))
# i = 0
# while user:
#     i = random.randint(1, 8)
#     i += 1
# print(i)

# num = 0
# i = 0

# num = int(input())
# while i < num:
#     j = 0
#     while j < num:
#         print((i+j) % num + 1, end=' ')
#         j += 1
#     print()
#     i += 1

# arr = ["박대성", "혜니", 9]
# num = 2
# for i in arr:
#     print("데이터 : ", end="\t")
