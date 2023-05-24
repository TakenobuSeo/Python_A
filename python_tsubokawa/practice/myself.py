import introduce

import sys 
args = sys.argv
print(args)

name = args[1]
age = args[2]

# introduce.pyよりIntroクラスを作成
intro1 = introduce.Intro(name, age)
print(intro1.get_name())
print(intro1.get_age())