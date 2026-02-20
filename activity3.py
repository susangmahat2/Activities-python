print("select your ride")
print("1. bike")
print("2. car")

choice=int(input("enter your choice: "))
if choice==1:
    print("what type of bike do you want?")
    print("1. Scooty\n")
    print("2.scooter\n")

    choosebike=int(input("enter your choice: "))
    if choosebike==1:
        print("you have selected scooty")
    elif choosebike==2:
        print("you have selected scooter")
    else:
        print("invalid choice")
elif choice==2:
    print("what type of car do you want?")
    print("1. sedan\n")
    print("2. suv\n")

    choice3=int(input("enter your choice: "))
    if choice3==1:
        print("you have selected sedan")
    elif choice3==2:
        print("you have selected suv")
    else:
        print("invalid choice")