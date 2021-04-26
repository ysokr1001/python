# a = [[0 for j in range(2)] for i in range(3)]
# print(a)

# a = [[0] * 2 for i in range(3)]
# print(a)

# a = [3, 1, 3, 2, 5]
# b = []

# TODO 내가 세운 식은 왜 안될까 아래 정답과 비교해보기 # 오우 됐져
# b = [3, 1, 3, 2, 5]
# a = [[0 for j in range(b[i])] for i in range(5)]
# print(a)

# a = [[0] * i for i in [3, 1, 3, 2, 5]]
# print(a)


# for i in a:
#     line = []
#     for j in range(i):
#         line.append(0)
#     b.append(line)

# print(b)

# a = [[10, 20], [30, 40]]
# b = a.copy()
# b[0][0] = 500
# print(a)
# print(b)

# import copy
# a = [[10, 20], [30, 40]]
# b = copy.deepcopy(a)
# b[0][0] = 500
# print(a)
# print(b)

# a = [[[0]*3 for i in range(4)] for y in range(2)]
# print(a)

# b = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
# print(b)

# s = 'hello, world!'
# s = s.replace('world', 'python')
# print(s)


# table = str.maketrans('aeiou', '12345')
# 'apple'.translate(table)
# print(table)

# b = 'apple pear grape pineapple orange'.split()
# print(b)

# a = 'python'.upper()
# print(a)

# a = 'PyThon'.lower()
# print(a)

# 공백은 모두 사라진다 l은 left
# a = '      python    '.lstrip()
# print(a)

# a = '      python    '.rstrip()
# print(a)

# a = '      python    '.strip()
# print(a)

# a = ', python.'.rstrip(',.')
# print(a)

# a = "'python'".rjust(10)
# print("'python'".rjust(10))

# a = 'python'.center(10)
# print(a)

# a = 'python'.rjust(10).upper()
# print(a)

# a = '35'.zfill(4)
# print(a)
# b = '3.5'.zfill(6)
# print(b)
# c = 'hello'.zfill(10)
# print(c)

# a = 'apple pineapple'.find('pl')
# print(a)

# b = 'apple pineapple'.find('xy')
# print(b)

# a = 'apple pineapple'.rfind('pl')
# print(a)

# b = 'apple pineapple'.rfind('xy')
# print(b)

# a = 'apple pineapple'.index('pl')
# print(a)

# b = 'apple pineapple'.index('xy')
# print(b)

# a = 'apple pineapple'.count('pl')
# print(a)

# b = 'apple pineapple'.count('xy')
# print(b)

# a = 'apple pineapple apple pineapple'.index('pl')
# b = a.index('pl')
# i = a.index('pl')
# print(a.index('pl'))
# print(a)
# print(b)

# strmy = 'apple pineapple'
# nfind1 = strmy.find('pl')
# print(nfind1)
# newnfind = nfind1 + 2
# strmy = strmy[newnfind:]
# nfind2 = strmy.find('pl')
# nfind2 = (newnfind) + nfind2
# print(nfind2)

# TODO 이해를 해보자 꼭꼭 안보고 짜보기
# str1 = '01001111'
# str2 = '1'

# cnt = str1.find(str2)
# print(cnt)

# while str1[cnt+1:].find(str2) != -1:
#     print(str1[cnt+1:].find(str2), "번째 인덱스")
#     cnt = str1[cnt+1:].find(str2) + cnt + 1
#     print(cnt)

# cnt = -1
# while str1[cnt+1:].find(str2) != -1:
#     cnt = str1[cnt+1:].find(str2) + cnt + 1
#     print(cnt)

# s = 'apple pineapple apple pineapple'
# count = 0
# a = 0
# ina = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# while True:
#     if count == len(s):
#         break
#     if s[count] == 'p' and s[count + 1] == 'l':
#         ina[a] = count
#         a += 1
#     count += 1
# print('count:', a)
# for i in range(len(ina)):
#     if ina[i] == 0:
#         break
#     print(ina[i])

# import re
# str1 = 'apple pineapple apple pineapple'
# str2 = 'pl'

# for a in re.finditer(str2, str1):
#     print(a.start(), a.end())

# print('I am %s' % 'james')
# name = 'maria'
# print('I am %s' % name)

# print('I an %d years old' % 20)

# print('%f' % 2.3)
# print('%.2f' % 2.3)
# print('%.3f' % 2.3)

# print('%10s' % 'python')
# print('%-10s' % 'python')

# print('Tday is %d %s' % (3, 'april'))
# print('Tday is %d%s' % (3, 'april'))

# print('Hello, {0}'.format('world!'))
# print('Hello, {0}'.format(100))

# print('Hello, {0} {2} {1}'.format('python', 'script', 3.6))
# print('{0} {0} {1} {1}'.format('python', 'script'))
# print('Hello, {} {} {}'.format('python', 'script', 3.6))

# print('Hello, {language} {version}'.format(language='python', version=3.6))

# language = 'python'
# version = 3.6
# print(f'hello,{language} {version}')

# print('{0:>10}'.format('python'))
# print('{0:>10} {2:>10}{1:<10}'.format('python', 'abc', 123))

# print('%03d' % 1)
# print('{0:03d}'.format(35))
# print('%08.2f' % 3.6)
# print('{0:08.2f}'.format(150.37))

# print('{0:0<10}'.format(15))
# print('{0:0>10}'.format(15))
# print('{0:0>10.2f}'.format(15))

# print('{0: <10}'.format(15))
# print('{0:>10}'.format(15))
# print('{0:x>10.2f}'.format(15))

# filename = []
# path = 'C:\\users\\edu\\appdata\\local\\proframs\\python\\python36-32\\data.txt'
# z = path.find('data.txt')
# filename.append(z)
# print(filename)

# x = path.split('\\')
# filename = x[-1]
# print(filename)

# x = path.split('\\')
# x.reverse()
# filename = x[0]

# filename = path[path.rfind('\\') + 1:]

# x = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."

# b = 'apple pineapple'.count('xy')
# print(b)

# b = x.count('the')
# print(b)

# print(str.count('the ') + str.count('the,') + str.count('the.'))
