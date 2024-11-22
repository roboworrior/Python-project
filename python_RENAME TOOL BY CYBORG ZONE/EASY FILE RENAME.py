import os 

print("##### EASY FILE RENAME TOOL ############")

#a=input("\nENTER THE CHARCTER YOU WANNA DELET : ")

arr=os.listdir("target")
arr2=os.listdir("target")

i=0
print("\n")
while i<len(arr): 
	print(arr[i])
	i=i+1
	
a=input("\nENTER THE CHARACHTERS YOU WANA REMOVE : ")
b=input("\nENTER THE CHARACHTERS YOU WANA REPLACE WITH : ")

i=0
while i<len(arr): 
	arr[i]=arr[i].replace(a,b)
	i=i+1
	
ch1:str="target/"
ch2:str="target/"

#ch1+=arr2[1]
#ch2+=arr[1]

i=0
while i<len(arr): 
	ch1+=arr2[i]
	ch2+=arr[i]
	
	os.rename(ch1,ch2)
	
	ch1:str="target/"
	ch2:str="target/"

	i=i+1
	




