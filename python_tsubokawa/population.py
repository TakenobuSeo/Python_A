countries = ("China", "India", "U.S.A", "Indonesia",
  "Pakistan", "Brazil", "Nigeria",
    "Bangladesh", "Russia", "Mexico")

# #入力値の取得
import sys
args = sys.argv

index = int(args[1])

print(countries[index-1])