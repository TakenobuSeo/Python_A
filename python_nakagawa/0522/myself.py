import introduce
import sys
args = sys.argv

# 引数に名前と年齢をいれる
name = args[1]
age = args[2]

intro = introduce.Intro(name, age)
intro.name_out()
intro.age_out()

# name = intro.name_out()
# age = intro.age_out()
# print(name)
# print(age)
