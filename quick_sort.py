def pivot_ele(arr,first,last):
    pivot=arr[first]
    left=first+1
    right=last

    while True:
        while left<=right and arr[left]<=pivot:
            left=left+1
        while left<=right and arr[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[right],arr[first]=arr[first],arr[right]
    return right



def quick_sort(arr,first,last):
    if first<last:
        p=pivot_ele(arr,first,last)
        quick_sort(arr,first,p-1)
        quick_sort(arr,p+1,last)


if __name__ == "__main__":
    arr=[8,9,6,3,2,4,7,5,20,10,16]
    n=len(arr)
    quick_sort(arr,0,n-1)
    print(arr)