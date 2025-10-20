# Code 25. Demonstrate break in for loop with else block
roll = int(input('Enter your roll (Only digit): '))
numbers = [11, 33, 55, 38, 55, 63, 45, 21, 23, 41]

for num in numbers :
    if num == roll :
        print ('Congratulations! You are selected')
        break
else :
    print ('You are not selected')

print ()
print ("Exiting...")