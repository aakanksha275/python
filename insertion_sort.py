def insertion(my_list):
    for index in range(1,len(my_list)):
        current_ele = my_list[index]
        pos=index
        while current_ele<my_list[pos-1] and pos>0:
            my_list[pos]=my_list[pos-1]
            pos=pos-1
        my_list[pos] = current_ele


num = int(input("entet number of elements"))
list1=[int(input())for i in range(num)]
print(list1)
insertion(list1)
print(list1)