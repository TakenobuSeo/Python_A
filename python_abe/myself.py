import introduce
import sys
args = sys.argv
name = args[1]
age = args[2]
myself = introduce.Intro(name,age)
print(myself.name_out())
print(myself.age_out())