import numpy as np
import math
def twin_prime(digits):

    start_no=10**(digits-1)
    end_no= 10**(digits)-1
    prime_list=[]
    for num in range(start_no,end_no+1):
        if num==3:	
            prime_list.append(num)
            continue
        if num%2 ==0 or num==1 or num==2:
            continue
        sqrt= int(math.sqrt(num))
        n=0
        for p in range(2,sqrt+1):
            if num%p !=0:
                n=n+1
        if n==sqrt-1:
            prime_list.append(num)  
    return prime_list

digit=int(input("enter number of digit decimals: "))

prime_list=twin_prime(digit)
f = open("myfile.txt", "w")
for i in range(len(prime_list)-1):
    if prime_list[i+1]-prime_list[i]==2:
        f.write("{} {}\n".format(prime_list[i],prime_list[i+1]))
f.close()
f=open("myfile.txt", "r")
print(f.read())