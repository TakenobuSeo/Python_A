import introfamily
import sys
args = sys.argv
name = args[1]
age = args[2]
cat = args[3]
def text_out(text):
    txt = "年齢は、" + text + "歳です"
    return txt
myself = introfamily.IntroFam(name,age,cat)
print(myself.name_out())
print(myself.age_out())
print(myself.cat_out())
print(text_out("aaa"))
print(myself.text_out("aaa"))