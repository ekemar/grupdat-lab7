#encoding: utf-8
class Node():
    def __init__(self, value=None, n=None):
        self.item = value
        self.next = n

class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
    
    def put(self, x):
        if self.top is None:
            self.top = Node(x)
            self.bottom = self.top
        else:
            n = Node(x)
            self.top.next = n
            self.top = n

    def isempty(self):
        if self.bottom is None:
            return True
        else:
            return False

    def get(self):
        if self.isempty():
            return None
        else:
            n = self.bottom
            self.bottom = self.bottom.next
            return n.item
