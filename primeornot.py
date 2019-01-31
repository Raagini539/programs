a=input()
num=0
for i in range(2,a//2+1):
  if(a%i==0):
    num=num+1
if(num<=0):
  print("yes")
else:
  print("no")
