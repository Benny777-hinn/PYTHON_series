cities=["bangl","cheni","guntr","hosur"]
heroes=["thor","iron man","king"]

def print_len(list):
    print(len(list))
          
    
print_len(cities)
print_len(heroes)
# this function will print the length of the list passed as an argument

def print_list(list):
    for item in list:
        print(item ,end=" ")
 
print_list(heroes)
# this function will print the items of the list passed as an argument

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

cal_fact(5)
# this function will calculate the factorial of the number passed as an argument

def converter(usd_val):
    inr_val= usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
    
converter(1)
converter(6)
converter(10) 
# this function will convert the given USD value to INR and print the result

def evn_odd(n):
    if(n%2==0):
        print("Nmber",n,"is EVEN")
    else:
        print("Number",n,"is ODD")
            
evn_odd(5)
evn_odd(4)
evn_odd(89)

# this function will check if the given number is even or odd and print the result accordingly.