arr=[34,81,2,9,6,54,5,7,6,33]

n=len(arr)

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
    
print(arr)