
def binarys(sarr,find):
    low=0
    high=n-1
    found=0
    while(found!=1 and low<=high):
        mid=(low+high)//2
        if find==sarr[mid]:
            found=1
            
        if find>sarr[mid]:
            low=mid+1
        else:
            high=mid-1

    if found==1:
        return mid
    else:
        print("key is not found")
    

arr=[7,9,6,5,4,1,8,19,3,2,4]
sarr=sorted(arr)
print(sarr)

n=len(sarr)
#print(n)
find=int(input("enter element to find"))
ans=binarys(sarr,find)
print(f"key is found at {ans}")