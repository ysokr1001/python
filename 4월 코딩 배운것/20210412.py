#lux = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
#lux['apple'] = 500
#print(lux) 

# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# print("변경전 딕셔너리는" , Fruits, "입니다")
# sel = int(input("변경된 바나나 가격을 입력하세요: "))
# sel1 = int(input("변경된 banana 가격을 입력하세요: "))
# sel2 = int(input("변경된  가격을 입력하세요: "))
# sel3 = int(input("변경된 파인애플 가격을 입력하세요: "))
# Fruits['apple'] = sel
# Fruits['banana'] = sel1
# Fruits['orange'] = sel2
# Fruits['pineapple'] = sel3
# print("변경된 딕셔너리는", Fruits, "입니다")

# Fruits = {'apple': 1000, 'banana': 700, 'orange': 1500, 'pineapple': 2000}
# print("변경전 딕셔너리는", Fruits , "입니다")
# sel = int(input("변경된 사과의 가격은: "))
# Fruits['apple'] = sel
# print("변경된 딕셔너리는", Fruits , "입니다")

# Fruits = {'apple': 0, 'banana': 0, 'orange': 0, 'pineapple': 0}
# a_i, b_i, o_i, p_i = map(int, input("과일의 가격을 순서대로 입력하시오:").split('/'))

# wow = dict(zip(['health', 'health_regen', 'mana', 'mana_regen'], [575.6, 1.7, 338.8, 1.63]))
# print(wow)

# d_key = input().split()
# d_value = map(float, input().split())
# d_out= dict(zip(d_key, d_value))
# print(d_out)

x = input().split()
y = x[len(x) -5: len(x)]
z = x[:len(x)-5]
print(y)
print(z)