n = int(input())

li1 = [1, 2, 3, 4, 5, 6]
li2 = [1, 2, 3, 4, 5, 6]
li3 = [1, 2, 3, 4, 5, 6]

sumrow = [x + y + z for x in li1 for y in li2 for z in li3]

if n in sumrow:
  print("Yes")
else:
  print("No")