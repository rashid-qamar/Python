#demonstrate nested if statements
marks = int(input("Enter your Marks: "))
if marks > 60 :
    if marks > 90 :
        print ("Your Grade: A+ \n")

    elif marks > 80 :
        print ("Your Grade: A \n")

    elif marks > 70 :
        print ("Your Grade: B \n")

    elif marks > 60 :
        print ("Your Grade: C \n")
    
else :
    if marks > 30 :
        print ("Better Luck, Next time \n")

    else :
        print ("Leave the course \n")