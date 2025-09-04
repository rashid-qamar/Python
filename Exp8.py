a = int(input("Enter first number(A): "))
b = int(input("Enter second number(B): "))

print ('A =', bin(a))
print ('B =', bin(b))

And = a & b
print ("result for AND is: ", bin(And))

Or = a | b
print ("result for OR is: ", bin(Or))

xor = a ^ b
print ("result for XOR is: ", bin(xor))

com1 = ~a
com2 = ~b
print ("Complement of A: ", com1, ": " bin(com1))
print ("Complement of B: ", com2, ": " bin(com2))

