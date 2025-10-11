#Demonstrate Using else Statement with Loops
number = [12, 23, 34, 38, 42, 45, 55, 18]

for num in number :
    if num%2 == 0 :
        print ('The list contain an Even number')
        break
    else :
        print ('The list does not contain Even Number')

print ('Exiting...')