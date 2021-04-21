# 89 83 94 같은 정보를 리스트로 바꿀 때
string = "89 83 94"
arr = list(map(int, string.split()))
print(arr)  # [89, 83, 94]
