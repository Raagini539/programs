sum = 0
num=input()
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 1
if(num == sum):
   print("yes")
else:
   print("no")
