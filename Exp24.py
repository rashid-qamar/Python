# Code 24. Demonstrate break
for letter in 'Dept of CS&IT' :
    if letter == '&' :
        break
    print ('Current Letter: ', letter)

num = 10
while num > 0 :
    print ('Current variable value: ', num)
    num = num - 1
    if num == 5 :
        break

print ("Exiting...")