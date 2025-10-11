## Code 12. Program showing how to give multiple inputs using split
x, y = input("Enter no. of Boys & Girls: ").split()        #Two input

print ("No. of Boys: ", x)
print ("No. of Girls: ", y)
print ("\n")

a, b, c = input("Enter no. of student of Group (A, b & C): ").split()   #Three input

print ("Group A is {}, Group B is {} and Group C is {}".format(a, b, c))
print ("\n")


x = list(map(int, input ("Enter numbers: ").split()))
print ("List of numbers: ", x)
print ("\n")

print ("Exiting...")