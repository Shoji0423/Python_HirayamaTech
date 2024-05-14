#foodに引数を代入
import sys
food = sys.argv[1]

#sentenceに変数を代入
sentence = "I don't like \"{0}\"".format(food)
print(sentence)