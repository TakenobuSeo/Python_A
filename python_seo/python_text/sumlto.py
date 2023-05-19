# 合計の初期値は0
v = 0

# 合計vに1－10を足していく
for i in range(1, 11):
    v = v + i
    print(i, "を足すと", v)

print("1から10を足すと", v)
