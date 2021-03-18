def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        l_list = list1[:mid]
        r_list = list1[mid:]
        mergesort(l_list)
        mergesort(r_list)
        i=0
        j=0
        k=0
        while i<len(l_list) and j<len(r_list):
            if l_list[i]<r_list[j]:
                list1[k]=l_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=r_list[j]
                j=j+1
                k=k+1
        
        while i<len(l_list):
            list1[k]=l_list[i]
            i=i+1
            k=k+1
        
        while j<len(l_list):
            list1[k]=r_list[j]
            j=j+1
            k=k+1

num = int(input("how many elements"))
list1=[int(input()) for x in range(num)]
mergesort(list1)
print(list1)