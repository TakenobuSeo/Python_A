animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]
import sys
args = sys.argv
i = int(args[1])
name = args[2]
animal_list.insert(i,name)
animal_list.pop()
print(sorted(animal_list),end="")