# Practice question 1: This code creates a file called "practice.txt" and writes three lines of text into it.

with open("practice.txt","w") as f:
    f.write("This is a practice file java.\n")
    f.write("It contains multiple lines of text.\n")
    f.write("This is the third line I will learn java .\n")

# Practice question 2: This code reads the content of "practice.txt", replaces all occurrences of "java" with "python", and prints the modified content.
with open("practice.txt","r") as f:
    content = f.read()

new_content = content.replace("java","python")
print(new_content)

# Practice question 3: This code reads the content of "practice.txt", counts the number of words in it, and prints the word count.
with open("practice.txt","r") as f:
    content = f.read()
    word_count = len(content.split())
    print("Word count:", word_count) 

# Practice question 4: This code reads the content of "practice.txt" and checks if the word "python" is present in it. It prints a message indicating whether the word is found or not.
with open("practice.txt","r") as f:
    content = f.read()
    if (content.find("python")!=-1):
        print("The word 'python' is present in the file."  )
    else:        
        print("The word 'python' is not present in the file." )

# Practice question 5: This code reads the content of "practice.txt" and checks if the word "learn" is present in it. It prints a message indicating whether the word is found or not.

def check_for_word(word): 
    
    with open("practice.txt","r") as f:
        content = f.read()
        if (content.find(word)!=-1): # if (word in content) can also be used instead of if (content.find(word)!=-1 )
            print(f"The word '{word}' is present in the file."  )
        else:        
            print(f"The word '{word}' is not present in the file." )
check_for_word("learn")
# Practice question 6: This code reads the content of "practice.txt" line by line and checks if the word "will" is present in any of the lines. If it finds the word, it prints the line number where the word is found. If the word is not found in any line, it returns -1.
def check_for_line():
    word="will"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())


# for this code we overwrite the content of file with array of numbers seperated by comma and then read the content of file and print it.
#Practice question 7: This code writes an array of numbers separated by commas into "practice.txt", reads the content of the file, splits the numbers, and counts how many of them are even. Finally, it prints the count of even numbers.
count=0
with open("practice.txt","r") as f:
    content = f.read()
    print(content)
    
    num=content.split(",")

    for val in num:
        if(int(val)%2==0):
            count+=1

print("Count of even numbers:", count)


