from ADT import ArrayQueue

x = ArrayQueue()

x.enqueue(5)
x.enqueue(3)
x.dequeue()
x.enqueue(2)
x.enqueue(8)
x.dequeue()
x.dequeue()
x.enqueue(9)
x.enqueue(1)
x.dequeue()
x.enqueue(7)
x.enqueue(6)
x.dequeue()
x.dequeue()
x.enqueue(4)
x.dequeue()
x.dequeue()

print(x._data)
