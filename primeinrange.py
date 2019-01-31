n1=input()
n2=input()
num=0
for i in range(n1,n2+1):
  for j in range(2,i//2):
    if(i%j==0):
      print(i)
    
