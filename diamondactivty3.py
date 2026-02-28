rows=int(input("enter the row:"))
if rows%2==0:
    halfdiamond=int(rows/2)
else:
    halfdiamond=int(rows/2)+1
space = halfdiamond-1
for i in range(1,halfdiamond+1):
    for j in range(1, space+1):
        print(end=" ")
    space= space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space = 1
for i in range (i, halfdiamond):
    for j in range(1 , space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range (1,2*(halfdiamond)):
        print(end=str(num))
        num=num+1
    print()
    space= space+1

