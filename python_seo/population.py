import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])

# タプルを作成
contries = (
        "China", "India", "U.S.A", "Indonesia", "Pakistan", 
        "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 引数の要素番号に当たるタプルの値を出力
print(contries[num])