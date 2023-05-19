
#国のタプル作成
countries = ("China", "India", "U.S.A", "Indonesia",
  "Pakistan", "Brazil", "Nigeria",
    "Bangladesh", "Russia", "Mexico")

# #入力値の取得
# import sys
# args = sys.argv

# index = int(args[1])

#デバッグ
index = 3
if (index<=0):
    print('エラー : 1以上の整数を入力してください')
else:
    print(countries[index-1], end="")