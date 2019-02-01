l=input()
r=input()
for i in range(l,r+1):
  for j in range(2,i):
    if(i%j!=0):
      print(i)
      
