# count=0
num=int(input("ENter a NUmber="))
# while(num>0):
#  num= num // 10
#  count +=1
# print(count)
from math import log10
n= log10(num)
countt=int(n)+1
print(countt)
  # palandrome
reverse=0
n=num
while(n >0):
 remainder=n % 10
 reverse=reverse*10 + remainder
 n=n//10
if num == reverse:
 print(reverse)
 print("palindrome")
else:
 print("Not a palindrome")




