from linked_list import LinkedList


class Queue_:
    def __init__(self, *args):
        self._queue = LinkedList()
        self.size = len(args)
        for arg in args:
            self._queue.insert_end(arg)

    def enqueue(self, val):
        self._queue.insert_end(val)
        self.size += 1

    def dequeue(self):
        if self._queue.start.next is self._queue.end:
            return None
        element = self._queue.start.next
        value = element.value
        element.delete()
        self.size -= 1
        return value

    def is_empty(self):
        return self._queue.start.next is self._queue.end

    def __repr__(self):
        return str(self._queue)



if __name__ == "__main__":
    q = Queue(1, 2, 3, 4, 5, 6, 7)
    x = q.dequeue()
    q.enqueue(8)
    print(x)
    print(q)
