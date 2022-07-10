
import random
array=[]

num = 100 -1 ;


while(len(array)<(num+1)):	
 randy = random.randint(0,num)
 try:
   array.index(randy)
 except ValueError:
   array.append(randy)
	  
print('array',array)
print("length of array",len(array))
# end of array prep
depth=[]
found=0
for i in range(len(array)):
	targetnum=i
	targetnum2=i
	count=50
	count2=50
	while(count!=0):
		count-=1
		if(targetnum2 != array[targetnum]):
			targetnum=array[targetnum ]
		else:
			depth.append(count2-count)
			found+=1;
			break;
print("found",found)
print('depth',depth)
			
	