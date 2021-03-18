arr=[7,9,6,5,4,1,8,19,3,2,4]



n=len(arr)


for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j    
    if arr[i]!=arr[min]:
        '''temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp'''
        arr[i],arr[min]=arr[min],arr[i]

print(arr)