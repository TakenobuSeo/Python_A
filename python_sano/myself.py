import sys
import introduce

args = sys.argv

person = introduce.Intro(args[1], int(args[2]))
print(person.name_out())
print(person.age_out())