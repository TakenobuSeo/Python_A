import introfamily
import sys
args = sys.argv

name = args[1]
age = args[2]
catName = args[3]

introFam = introfamily.IntroFam(name, age, catName)

# introFam.name_out()
# introFam.age_out()
# introFam.cat_out()
introFam.all_out()