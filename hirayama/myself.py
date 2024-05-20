from introduce import Intro
import sys 

args=sys.argv
name=args[1]
age=args[2]
intro=Intro(name,age)
print(intro.name_out())
print(intro.age_out())