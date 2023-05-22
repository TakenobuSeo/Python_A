import sys
args = sys.argv

rank = int(args[1])
rankList = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(rankList[rank - 1], end="")