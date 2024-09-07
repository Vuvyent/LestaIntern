# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

# В данном задани представлены две реализации циклической очереди: одна с использованием массива (т.к. в Python нет
# статических массивов, для его симуляции был использовать объект типа list с ограниченнием по размеру), и вторая -
# с использованием связного списка и неограниченного размера.
# Вторая реализация позволяет значительно проще сделать очередь неограниченного размера. Работа с циклической очередью
#на основе массива выполняется быстрее, т.к. процессору легче работать с данными, расположенными друг за другом.

# Первая реализация

class CycleQueue:
    def __init__(self, size):
        self.data = [0 for i in range(size)]
        self.size = size
        self.front = -1
        self.rear = -1

    def is_full(self):
        if self.front == self.rear + 1 or (self.front == 0 and self.rear == self.size - 1):
            return 1
        else:
            return 0

    def is_empty(self):
        if self.front == -1:
            return 1
        else:
            return 0

    def push(self, elem):
        if self.is_full():
            raise Exception("Queue is full! Unable to add an element")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = elem
            print(self.data)

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty! Unable to remove an element")
        else:
            elem = self.data[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1)%self.size
                print(elem)
                return elem


# Вторая реализация
class Node:
    def __init__(self, elem):
        self.value = elem
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = self.front

    def is_empty(self):
        if self.front is None:
            return 1
        else:
            return 0

    def push(self, elem):
        new_node = Node(elem)
        if self.front is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty! Unable to remove an element")
        else:
            result = self.front.value

            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.rear.next = self.front

            return result

    def print_queue(self):
        if self.front is None:
            print("queue is empty")
        else:
            curr = self.front
            while curr is not self.rear:
                print(curr.value, end=" ")
                curr = curr.next
            print(curr.value)


if __name__ == "__main__":
    myCycleQueue = CycleQueue(5)
    myLinkedListQueue = LinkedListQueue()
    try:
        myCycleQueue.push(5)
        myCycleQueue.push(4)
        myCycleQueue.push(3)
        myCycleQueue.push(2)
        myCycleQueue.push(1)
        myCycleQueue.pop()
        myCycleQueue.push(9)
    except Exception as e:
        print(e)

    try:
        myLinkedListQueue.push(2)
        myLinkedListQueue.print_queue()
        myLinkedListQueue.push(3)
        myLinkedListQueue.print_queue()
        myLinkedListQueue.push(4)
        myLinkedListQueue.print_queue()
        myLinkedListQueue.push(5)
        myLinkedListQueue.print_queue()
        myLinkedListQueue.pop()
        myLinkedListQueue.print_queue()
        myLinkedListQueue.pop()
        myLinkedListQueue.print_queue()
        myLinkedListQueue.pop()
        myLinkedListQueue.print_queue()
        myLinkedListQueue.pop()
        myLinkedListQueue.print_queue()

    except Exception as e:
        print(e)




