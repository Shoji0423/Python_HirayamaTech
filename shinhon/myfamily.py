from mod.introfamily import IntroFam
import sys

input = sys.argv

owner = str(sys.argv[1])
age = str(sys.argv[2])
pet = str(sys.argv[3])

info = IntroFam(owner, age, pet)
print(info.name_out())
print(info.age_out())
print(info.cat_out())