import sys
input = int(sys.argv[1])

if input >= 1 and input <= 200:
    for i in range(input):
        print("ひつじが{0}匹".format(i+1))