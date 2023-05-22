import sys
import introfamily

args = sys.argv
person = introfamily.IntroFam(name = args[1], age = args[2], cat_name = args[3])
print(person.name_out())
print(person.age_out())
print(person.cat_out())