class LinkedList:
    def __init__(self):
        self.head = None

    @property
    def node(self):
        return self._node
    
    @node.setter
    def node(self, node):
        self._node = node

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


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next    

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val