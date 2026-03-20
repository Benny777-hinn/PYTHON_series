f=open("demo.txt","rt")
data=f.read()
print(data)
print(type(data))
f.close()
# The above code opens a file named "demo.txt" in read mode, reads its entire content, prints it, and then prints the type of the data (which will be a string). Finally, it closes the file.

f=open("demo.txt","r")
data=f.read(5)
print(data)
print(type(data))
f.close()   # The above code opens the same file but reads only the first 5 characters, prints them, and then prints the type of the data (which will still be a string). Finally, it closes the file.

f=open("demo.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close() 
# The above code opens a file named "demo.txt" in read mode, reads the first line, prints it, reads the second line, prints it, and then closes the file.