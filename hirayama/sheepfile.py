import sys
args=sys.argv
number=int(args[1])
a_file=open("../../files/sheep.txt",mode="w",encoding="utf-8")
for i in range(1,number+1) :
    a_file.write("ひつじが{0}匹\n".format(i))

a_file.close()