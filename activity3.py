num=int(input("Enter a number: "))
sum=0
for i in range(num,0,-1):
    sum=sum+i
    
    print(i)

print("The sum of numbers from", num, "to 1 is:", sum)
