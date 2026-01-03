## Code 54. Demonstrate Write file with appending the content to file
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#for open & Reading
f = open("demofile.txt", "r")
for x in f:
    print(x)
print()
