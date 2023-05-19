import sys

args = sys.argv
output_index = int(args[1])-1
ranking_population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(ranking_population[output_index], end="")