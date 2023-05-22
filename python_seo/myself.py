import introduce
import sys
args = sys.argv

name = args[1]
age = args[2]

intro = introduce.Intro(name, age)
print(intro.name_out())
print(intro.age_out())