class LinkedList:
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head):
        self._head = head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def size(self):
        count = 0
        for node in self:
            count = count + 1
        return count


class Node:
    def __init__(self, val):
        self._val = val
        self._next = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    def __repr__(self):
        return self._val