import sys
args=sys.argv
number=int(args[1])
add_animal=args[2]
animal=["giraffe", "tiger", "zebra", "elephant", "lion"]
animal.insert(number,add_animal)
animal.pop()
animal.sort()
print(animal)