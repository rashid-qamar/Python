#Demonstrate Using uses a nested-for loop to display multiplication tables from 1-10
for i in range (1,11) :
    for j in range (1,11) :
        k = i*j
        print (k, end = '\t')
    print ()