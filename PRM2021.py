import random
import array
Correct=0
Tries=0
RandMultiplier=[0,0,0,0,0]
print("This is a program for kiddos to learn multiplication\n")
while True:
        StudentName=input("Enter your name :\n")
        StudentName.rstrip()
        if StudentName=="":
            print("Please enter sensible values for your name\n")
        elif any(not c.isalnum() for c in StudentName):
            print("Can you please enter sensible values and not integers/special characters\n")
        elif StudentName.isdigit():
            print("Please enter values which are NOT integers")
        else:
            print("Thank You for entering correct values , you may now proceed with your test\n")
            break;
print("""
Choose one of the following-
1:Testing\n
2:Learning\n
""")
while True:
    FirstChoice=input("Enter 1 or 2 according to what you need :")
    if FirstChoice=="1":
        print("You have chosen to get tested \n")
        print("""
You can choose multiplication tables from 2 to 12,
Please enter a value from the given range\n
""")
        while True:
            MultiCh=input("Enter a value from the above range\n")
            if MultiCh.isdigit():
                if int(MultiCh)>12 or int(MultiCh)<2 :
                    print("Please enter a number from the given range\n")
                else:
                    MultiCh=int(MultiCh)
                    break;
            else:
                print("Please enter sensible values")
        for i in range(5):
            
            RandMultiplierVar=random.randint(1,12)
            while RandMultiplierVar in RandMultiplier:
                RandMultiplierVar=random.randint(1,12)
            RandMultiplier[i]=RandMultiplierVar
            print(" What is "+str(MultiCh)+" x " +str(RandMultiplierVar)+"\n")
            while True:
                TestAnswer=input("Enter the answer :\n")
                if TestAnswer=="":
                    print("Please enter a number")
                elif TestAnswer.isdigit():
                    break;
                else:
                    print("Please enter sensible values and not letters")
            if TestAnswer==MultiCh*RandMultiplierVar:
                  Correct=Correct+1
        print(StudentName +", you got "+str(Correct)+"/5\n")
        if Correct==5:
            print("Congratulations !!\n")
        elif Correct==0 or Correct==1 or Correct==2:
            print("You need to try harder , better luck next time!!\n")
        else:
            print("You can perform better!!\n")
        break;
    elif FirstChoice=="2":
        print("You have chosen to learn \n")
        print("""
You can choose multiplication tables from 2 to 12,
Please enter a value from the given range\n
""")
        while True:
            MultiCh=input("Enter a value from the above range\n")
            if MultiCh.isdigit():
                if int(MultiCh)>12 or int(MultiCh)<2:
                    print("Please enter a number from the given range\n")
                else:
                    MultiCh=int(MultiCh)
                    break
            else:
                print("Please enter sensible values")
        for i in range(5):
            Tries=0
            RandMultiplierVar=random.randint(1,12)
            while True:
                if RandMultiplierVar not in RandMultiplier:
                    break
                else:
                    RandMultiplierVar=random.randint(1,12)
            RandMultiplier[i]=RandMultiplierVar
            while Tries<3:
                print(" What is "+str(MultiCh)+" x " +str(RandMultiplierVar)+"\n")
                while True:
                    TestAnswer=input("Enter the answer :\n")
                    if TestAnswer=="":
                        print("Please enter a number\n")
                    elif TestAnswer.isdigit():
                        break;
                    else:
                        print("Please enter sensible values and not letters\n")
                if TestAnswer==str(MultiCh*RandMultiplierVar):
                    print(StudentName + ", your answer is correct ,very good\n")
                    break;
                elif TestAnswer>str(MultiCh*RandMultiplierVar):
                    print(StudentName +", your answer is larger than the actual answer\n")
                    Tries=Tries+1
                    if Tries==3:
                        print("The correct answer was ," +str(MultiCh*RandMultiplierVar)+"\n")
                elif str(MultiCh*RandMultiplierVar)>TestAnswer:
                    print(StudentName +", your answer is smaller than the actual answer\n")
                    Tries=Tries+1
                    if Tries==3:
                        print("The correct answer was ," +str(MultiCh*RandMultiplierVar)+"\n")

        break;
    else:
        print("You have entered an incorrect value , please re enter a valid choice (1 or 2) \n")
        
        
