class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData (self):
        return self.data
    def getNext (self):
        return self.next
    def setData (self, newdata):
        self.data = newdata
    def setNext (self, newnext):
        self.next = newnext

class UnorderedList():
    def __init__(self):
        self.head = None
    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
        return lstr
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
L = UnorderedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)
print(f'Lista antes: {L}')