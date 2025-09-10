## Code 8. Demonstrate Bitwise Operators
a = int(input("Enter first number(A): "))
b = int(input("Enter second number(B): "))

print ('A =', bin(a))
print ('B =', bin(b))

And = a & b
print ("result for AND is ", And, ": ", bin(And),"\n")

Or = a | b
print ("result for OR is ", Or, ": " , bin(Or),"\n")

xor = a ^ b
print ("result for XOR is ", xor, ": ", bin(xor),"\n")

com1 = ~a
com2 = ~b
print ("Complement of A ", com1, ": ", bin(com1))
print ("Complement of B ", com2, ": ", bin(com2),"\n")

lshift = a<<2;
print ("Left shift of A", lshift, ": ", bin(lshift),"\n")

rshift = a>>2;
print ("Right shift of A ", rshift, ": ", bin(rshift),"\n")