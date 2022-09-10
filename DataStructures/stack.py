from linked_list import LinkedList

class Stack:
    def __init__(self, *args):
        self._stack = list(*args)

    def pushback(self, value):
        self._stack.append(value)

    def pop(self):
        self._stack.pop(-1)