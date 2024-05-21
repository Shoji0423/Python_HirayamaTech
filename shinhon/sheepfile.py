import sys, os
input = int(sys.argv[1])

output_file = open(os.path.join("../..", "files", "sheep.txt"), mode="w", encoding="utf-8")

if input >= 1 and input <= 200:
    for i in range(input):
        # print("ひつじが{0}匹".format(i+1))
        # print(f"ひつじが{i+1}匹")
        output_file.write(f"ひつじが{i+1}匹 \n")