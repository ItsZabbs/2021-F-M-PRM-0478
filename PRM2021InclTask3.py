# importing libs
import random

# declaring variables
Correct = 0
Tries = 0
FirstQ = "n"
# starting program
print("This is a program for kiddos to learn multiplication\n")
print("""
Choose one of the following-
1:Testing\n
2:Learning\n
""")
# choosing input for Testing or learning
while True:
    FirstChoice = input("Enter 1 or 2 according to what you need :")
    if FirstChoice == "1":
        print("You have chosen to get tested \n")
        while True:
            StudentName = input("Enter your name :\n")
            StudentName = StudentName.rstrip()
            if StudentName == "":
                print("Please enter sensible values for your name\n")
            elif any(not c.isalnum() for c in StudentName):
                print("Can you please enter sensible values and not integers/special characters\n")
            elif StudentName.isdigit():
                print("Please enter values which are NOT integers")
            else:
                print("Thank You for entering correct values , you may now proceed with your test\n")
                break;
        while True:
            MixedCh = input("Do you want to get mixed numbers as the multiplier? (Y/N)")
            if MixedCh == "Y" or MixedCh == "y" or MixedCh == "N" or MixedCh == "n":
                break
            else:
                print("Please enter either Y or N")
        while True:
            QuestionCh = input("Please enter the number of questions you want in the test : ")

            if QuestionCh.isdigit():
                QuestionCh = int(QuestionCh)
                if QuestionCh < 2:
                    print("You cannot opt for less questions than the default number")
                elif QuestionCh > 12 and (MixedCh == "n" or MixedCh == "N"):
                    print("You cannot have more than 12 questions for a custom test")
                elif QuestionCh > 132 and (MixedCh == "Y" or MixedCh == "y"):
                    print("You cannot have more than 132 questions for a mixed test")
                else:
                    break;
            else:
                print("Please enter Numerical Values only")
        if MixedCh == "Y" or MixedCh == "y":
            RandTries = [None] * QuestionCh
            for i in range(QuestionCh):
                RandMultiplier1Var = random.randint(1, 12)
                RandMultiplier2Var = random.randint(2, 12)
                if FirstQ == "n":
                    RandTries[i] = ("" + str(RandMultiplier1Var) + "," + str(RandMultiplier2Var) + "")
                    FirstQ = "Y"
                else:
                    for z in range(len(RandTries)):
                        while True:
                            if RandTries[z] == "" + str(RandMultiplier1Var) + "," + str(RandMultiplier2Var) + "":
                                RandMultiplier1Var = random.randint(1, 12)
                                RandMultiplier2Var = random.randint(2, 12)
                            else:
                                RandTries[i] = ("" + str(RandMultiplier1Var) + "," + str(RandMultiplier2Var) + "")
                                break
                print("Question No :" + str(i + 1) + "\n")
                print(" What is " + str(RandMultiplier2Var) + " x " + str(RandMultiplier1Var) + "\n")
                while True:
                    Answer = input("Enter the answer :\n")
                    if Answer == "":
                        print("Please enter a number\n")
                    elif Answer.isdigit():
                        break;
                    else:
                        print("Please enter sensible values and not letters\n")
                if Answer == str(RandMultiplier2Var * RandMultiplier1Var):
                    Correct = Correct + 1
        else:
            print("""
You can choose multiplication tables from 2 to 12,
Please enter a value from the given range\n
""")
            while True:
                MultiCh = input("Enter a value from the above range\n")
                if MultiCh.isdigit():
                    if int(MultiCh) > 12 or int(MultiCh) < 2:
                        print("Please enter a number from the given range\n")
                    else:
                        MultiCh = int(MultiCh)
                        break
                else:
                    print("Please enter sensible values\n")
            RandMultiplier1 = []
            for i in range(QuestionCh):
                RandMultiplier1Var = random.randint(1, 12)
                while True:
                    if RandMultiplier1Var not in RandMultiplier1:
                        break
                    else:
                        RandMultiplier1Var = random.randint(1, 12)
                RandMultiplier1.append(RandMultiplier1Var)
                print("Question No :" + str(i + 1) + "\n")
                print(" What is " + str(MultiCh) + " x " + str(RandMultiplier1Var) + "\n")
                while True:
                    Answer = input("Enter the answer :\n")
                    if Answer == "":
                        print("Please enter a number")
                    elif Answer.isdigit():
                        break;
                    else:
                        print("Please enter sensible values and not letters")
                if Answer == str(MultiCh * RandMultiplier1Var):
                    Correct = Correct + 1
        print(StudentName + ", you got " + str(Correct) + "/" + str(QuestionCh) + "\n")
        if Correct == QuestionCh:
            print("Congratulations !!\n")
        elif Correct == 0 or Correct == 1 or Correct == 2:
            print("You need to try harder , better luck next time!!\n")
        else:
            print("You can perform better!!\n")
            break;
        break
    elif FirstChoice == "2":
        print("You have chosen to learn \n")
        while True:
            StudentName = input("Enter your name :\n")
            StudentName = StudentName.rstrip()
            if StudentName == "":
                print("Please enter sensible values for your name\n")
            elif any(not c.isalnum() for c in StudentName):
                print("Can you please enter sensible values and not integers/special characters\n")
            elif StudentName.isdigit():
                print("Please enter values which are NOT integers")
            else:
                print("Thank You for entering correct values , you may now proceed with learning tables\n")
                break;
        print("""
You can choose multiplication tables from 2 to 12,
Please enter a value from the given range\n
""")
        while True:
            MultiCh = input("Enter a value from the above range\n")
            if MultiCh == "":
                print("Please enter sensible values\n")
            elif int(MultiCh) > 12 or int(MultiCh) < 2:
                print("Please enter a number from the given range\n")
            else:
                MultiCh = int(MultiCh)
                break;
        RandMultiplier = [None] * 5
        for i in range(5):
            if Tries == 3:
                print("The correct answer was ," + str(MultiCh * RandMultiplierVar) + "\n")
            Tries = 0
            RandMultiplierVar = random.randint(1, 12)
            while RandMultiplierVar in RandMultiplier:
                RandMultiplierVar = random.randint(1, 12)
            RandMultiplier[i] = RandMultiplierVar
            while Tries < 3:
                print("Question No :" + str(i + 1))
                print(" What is " + str(MultiCh) + " x " + str(RandMultiplierVar) + "\n")
                while True:
                    Answer = input("Enter the answer :\n")
                    if Answer == "":
                        print("Please enter a number\n")
                    elif Answer.isdigit():
                        break
                    else:
                        print("Please enter sensible values and not letters\n")
                if Answer == str(MultiCh * RandMultiplierVar):
                    print(StudentName + ", your answer is correct ,very good\n")
                    break
                elif Answer > str(MultiCh * RandMultiplierVar):
                    print(StudentName + ", your answer is larger than the actual answer\n")
                    Tries = Tries + 1
                elif str(MultiCh * RandMultiplierVar) > Answer:
                    print(StudentName + ", your answer is smaller than the actual answer\n")
                    Tries = Tries + 1
        break
    else:
        print("You have entered an incorrect value , please re enter a valid choice (1 or 2) \n")
