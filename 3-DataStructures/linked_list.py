class StartPosition:
    def __init__(self):
        self.next = None
        self.value = "<"

    def get_next(self):
        return self.next

    def __repr__(self):
        return str(self.value)


class EndPosition:
    def __init__(self):
        self.previous = None
        self.value = ">"

    def get_previous(self):
        return self.previous

    def __repr__(self):
        return str(self.value)


class LinkedElement:
    def __init__(self, val, prev, next):
        self.value = val
        self.previous = prev
        self.next = next

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def delete(self):
        self.previous.next = self.next
        self.next.previous = self.previous
        del self

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.start = StartPosition()
        self.end = EndPosition()
        self.start.next = self.end
        self.end.previous = self.start

    def insert_end(self, val):
        element = LinkedElement(val, self.end.previous, self.end)
        self.end.previous.next = element
        self.end.previous = element

    def insert_start(self, val):
        element = LinkedElement(val, self.start, self.start.next)
        self.start.next.previous = element
        self.start.next = element

    def search(self, val) -> LinkedElement:
        s = self.start
        while not isinstance(s, EndPosition):
            s = s.next
            if s.value == val:
                return s
        return None

    def delete(self, val):
        el = self.search(val)
        if el is not None:
            el.delete()

    def __repr__(self):
        s = self.start
        r = ''
        while not isinstance(s, EndPosition):
            r += str(s)
            r += ' '
            s = s.get_next()
        r += str(self.end)
        return r


if __name__ == '__main__':
    l = LinkedList()
    l.insert_end(1)
    l.insert_end(2)
    l.insert_start(0)
    print(l)
    l.delete(1)
    print(l)
    x = l.search(1)
    print(x)
