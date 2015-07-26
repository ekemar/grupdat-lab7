#encoding: utf-8


class Queue:
    """Usage:
    q = Queue()

    q.put(x)             #sätter in x (sist) i kön

    q.isempty()          #ger True eller False
    
    q.get()              #tar ut och returnerar första elementet,
                         #returnerar None om kön är tom
    """
    
    def __init__(self):
        self.queue = []
    
    def put(self, x):
        self.queue.append(x)

    def isempty(self):
        if self.queue:
            return False
        else:
            return True

    def get(self):
        if self.isempty():
            return None
        else:
            return self.queue.pop(0)
        
    def __repr__(self):
        return "<Queue>"
    
