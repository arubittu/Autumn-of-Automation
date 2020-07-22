import numpy as np
import math	
palindrome= int(input('enter palindrome here: '))

def palindrome_checker(num):
  no_digits=len(str(num))
  string_num=str(num)
  req_loops=int(no_digits/2)
  placeholder=0
  for i in range(req_loops):
    if string_num[i]==string_num[-(1+i)]:
      placeholder=placeholder+1
  if placeholder==req_loops:
    return True
  else:
    return False
def next_palindrome(palindrome):
  num=palindrome
  while True:
    num=num+1
    if palindrome_checker(num)==True:
      return num
print(next_palindrome(palindrome))