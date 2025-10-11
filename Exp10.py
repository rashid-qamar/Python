## Code 10. Demonstrate Identity operator
a = int(input("Enter first number(A): "))
b = int(input("Enter second number(B): "))

print ("A = ", a, ": ", id(a))
print ("B = ", b, ": ", id(b))

if(a is b) :
    print ("A & B have same identity")
else :
    print ("A & B have NOT same identity")
