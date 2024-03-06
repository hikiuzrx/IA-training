import random
x = random.randint(1,10)
print(x)
y = 0
while y!=x :
     y = int(input("enter something : "))
     if x > y :
          print('try lil higher')
     elif y>x:
          print("try lil lower ")
     else:
          print(" just right")