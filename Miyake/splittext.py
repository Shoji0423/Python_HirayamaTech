import sys
args = sys.argv

#引数を変数に代入
text = str(args[1])#英文
number = int(args[2])#ｎ番目の単語

#分割
splittext = text.split()
print(splittext[number-1],end="")