import sys
# 挿入する場所の番号を代入
animal_pos = int(sys.argv[1])
# 挿入する動物の名前を代入
animal = sys.argv[2]

# 動物のリストを作成して、動物を挿入する
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(animal_pos, animal)

# 最後の動物を削除する
animals.pop()

# 並び方を変える
animals.sort()
print(animals)