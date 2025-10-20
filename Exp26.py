# Code 26. Demonstrate continue
for letter in 'University' :
    if letter == 'e' :
        continue
    print ('Current letter: ', letter)


num = 10
while num < 0 :
    print ('Current variable value: ', num)
    num = num - 1
    if num == 5 :
        continue

print ()
print  ("Exiting...")