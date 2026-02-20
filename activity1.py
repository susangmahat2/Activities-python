medical=input("Do you have medical cause?(Y/N):  ").strip().upper()
if medical=="Y":
    print("you can attend the exam")
else:
    attendence=int(input("What is your attendence percentage? "))
    if attendence>=75:
        print("you can attend the exam")
    else:
        print("you cannot attend the exam")