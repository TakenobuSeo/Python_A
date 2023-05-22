import sys
args = sys.argv

position = int(args[1])
animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animals.insert(position, animal)
animals.pop()
animals.sort()
print(animals, end="")
