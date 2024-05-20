from introfamily import IntroFam as fa
import sys
args=sys.argv
name=args[1]
age=args[2]
cat_name=args[3]
intro=fa(name,age,cat_name)
print(intro.name_out())
print(intro.age_out())
print(intro.cat_out())
