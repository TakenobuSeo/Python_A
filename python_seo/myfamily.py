import introfamily
import sys
args = sys.argv

name = args[1]
age = args[2]
cat = args[3]


intro_f = introfamily.IntroFamily(name, age, cat)
print(intro_f.name_out())
print(intro_f.age_out())
print(intro_f.cat_out())