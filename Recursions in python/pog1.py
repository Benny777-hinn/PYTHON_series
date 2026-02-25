# RECURSION to print n,n-1,n-2..... (function calls itself)
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)  # Recall of the same function
              # 1st checks if condition & if condition fails it prints
              #then show(n-1) will go through the 1st step until n==0
show(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(10))  #print function is always imp to print output