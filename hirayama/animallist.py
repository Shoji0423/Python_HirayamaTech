import sys
args=sys.argv
number=int(args[1])
add_animal=args[2]
animal=["giraffe", "tiger", "zebra", "elephant", "lion"]
#指定した位置に動物名を追加
animal.insert(number,add_animal)
#リストの末尾の要素を削除
animal.pop()
#ソート
animal.sort()
print(animal)