#48. Find the second largest number in a list.
list=[9,3,2,4,5,6]
length=len(list)
for i in range(0,length):
    for j in range(i+1,length):
        if(list[i] > list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("Second Largest Number is ",list[-2])


