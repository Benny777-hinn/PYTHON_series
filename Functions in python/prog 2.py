def cal_sum(a,b):  #we define a function called cal_sum that takes two parameters a and b.
    sum=a+b            # some work or set of statements is given
    print("The sum is",sum)
    return sum

cal_sum(3,9)
cal_sum(2,9)   # we can call the function as many times as we want with different arguments.

#the above function cal_sum takes two numbers as input and calculates their sum, prints it and returns the sum. We can use this function to calculate the sum of any two numbers by passing them as arguments when calling the function.

def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(int(avg))
    return avg
cal_avg(1,2,3)

#the above function cal_avg takes three numbers as input, calculates their sum, then calculates the average by dividing the sum by 3, prints the average as an integer and returns the average. We can use this function to calculate the average of any three numbers by passing them as arguments when calling the function.