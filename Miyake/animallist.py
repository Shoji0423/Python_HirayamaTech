import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])
animal = str(args[2])
#動物の名前リスト定義
animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]
#動物名を挿入
animal_list.insert(number,animal)
#一番後ろを削除
animal_list.pop()
#昇順に並び替える
animal_list.sort()
print(animal_list,end="")


