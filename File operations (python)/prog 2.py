f=open("demo.txt","w")
data=f.write("Hello, this is a demo file.\nThis file is used for demonstrating file handling in Python.")
f.close()
# The above code opens a file named "demo.txt" in write mode, writes a string to it, and then closes the file. If the file does not exist, it will be created. If it already exists, its content will be overwritten.

f=open("demo.txt","a")
data=f.write("about to learn file handling.\nThis file is used for demonstrating file handling in Python.")
f.close()
# The above code opens the same file in append mode, writes the same string to it, and then closes the file. This will add the new content to the end of the existing content without overwriting it.

f=open("sample.txt","w")
f.close()
# The above code creates an empty file named "sample.txt" by opening it in write mode

f=open("sample.txt","r+")
f.write("abc")
f.close()
# The above code opens the "sample.txt" file in read and write mode, writes the

f=open("sample.txt","r+")
data=f.read()
print(data)
f.close()
# The above code opens the "sample.txt" file in read mode, reads its content  it will append "abc" to the end of the file, and then closes the file. The content of the file will now be "abc". 

f=open("sample.txt","w+")
f.write("wbc")
f.close()
# The above code opens the "sample.txt" file in write and read mode, writes " wbc" to it, and then closes the file. This will overwrite any existing content in the file.