def clac_sum(n):
    if(n==0):
        return 0
    else:
        return clac_sum(n-1)+n
print(clac_sum(5)) 

#this above recursive function provides sum of n natural numbers

def print_lst(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx],end=" ")
    print_lst(list,idx+1)
    
fruits=["mango","lemon","apple"]
print_lst(fruits)

# The above function prints the elements of the list one by one using recursion. It takes a list and an optional index parameter (default is 0). If the index reaches the length of the list, it returns. Otherwise, it prints the current element and calls itself with the next index.