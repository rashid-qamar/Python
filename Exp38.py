##Code 38. Demonstrate Local and global variable
total = 0
#defining a function
def sum (a, b) :
    total = a+b
    print ("Total(Inside Function): ", total)
    return total
sum (10, 20)

print ()
print ("Total(Outside Function): ", total)