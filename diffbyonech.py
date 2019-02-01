#raagini
#EEE
count=0
strww=input().split()
str1=strww[0]
str2=strww[1]

for i in range(0,len(str1)):
  for j in range(0,len(str2)):
    if(str1[i]!=str2[j]):
      count=count+1
if(count==1):
  print("yes")
else:
	print("no")
