'''
1st method

q=[]
q.append(55)
q.append(15)
q.append(25)
q.sort(reverse=True)
print(q)

2nd method

import queue
q=queue.PriorityQueue()
q.put(60)
q.put(20)
q.put(10)
q.put(20)
print(q.get())
print(q.get())
print(q.get())
print(q.get())

3rd Method'''
q=[]
q.append((1,"aman"))
q.append((9,"aakanksha"))
q.append((6,"vishu"))
q.sort(reverse=True)
print(q)

