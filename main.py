import random

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]

#1
#for row in picture:
  #for pixel in row:
   #     if pixel == 1:
  #          print("*", end="")
     #   else:
     #       print(" ", end="")
  # print()


#2
#nota=int(input("nota:"))
# if nota<5:
#     print("reexaminare")
# elif nota>=5 and nota<=6 :
#     print("suficient")
# elif nota>=7 and nota<=8 :
#     print("bine")
# elif nota >= 9 and nota <=10:
#     print("excelent")

#3

import random
numar=random.randint(1,50)
nr=int(input("nr:"))
print("nr:",nr)
c=1
while nr!=numar:
    if nr>numar:
        c=c+1
        print("nr este mai mic")
    else:
        c=c+1
        print("nr este mai mare")
        nr=int(input("nr:"))
        print("nr:",nr)
        print("felicitari,ai ghicit numarul din",c,"incercari")
        print()
        print(numar)