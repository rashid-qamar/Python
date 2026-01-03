## Code 9. Demonstrate Membership Operators
a = int(input("Enter your roll no. (Only digit): "))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if(a in list) :
    print ("Your roll number is there in list !")
elif(a not in list) :
    print ("Your roll number is not there in list !")
