class LinkedListNode:
    """
    Contains a single node in a linked list
    Tracks the previous and next node
    """

    data = None
    previousNode = None
    nextNode = None

    def __init__(self, data) -> None:
        self.data = data
    
    def __repr__(self) -> str:
        return f"Data: {self.data}"

class HarrysLinkedList:
    """
    Double linked list
    """

    head = None
    tail = None
    count : int = 0

    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        nodes = []
        currentNode = self.head

        nodes.append("[")

        while currentNode != None:
            if currentNode is self.head:
                nodes.append(f"(Head: {currentNode.data}) > ")
            elif currentNode is self.tail:
                nodes.append(f"(Tail: {currentNode.data})")
            else:
                nodes.append(f"({currentNode.data}) > ")
            currentNode = currentNode.nextNode
        
        nodes.append("]")
        return "".join(nodes)

    def is_empty(self) -> bool:
        return self.head == None
    
    def size(self) -> int:
        return int(self.count)
    
    def appendItem(self, data) -> None:
        """
        Adds an item to the end of the list
        Increases the size by 1
        """
        newNode = LinkedListNode(data)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            newNode.previousNode = self.tail
            oldTail = self.tail
            oldTail.nextNode = newNode
            self.tail = newNode
            self.count += 1

    def prependItem(self, data) -> None:
        """
        Adds an item to the beginning of the list
        Increases the size by 1
        """
        newNode = LinkedListNode(data)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            newNode.nextNode = self.head
            oldHead = self.head
            oldHead.previousNode = newNode
            self.head = newNode
            self.count += 1

    def removeItem(self, index: int) -> None:
        """
        Takes an item at the given indext out of the list
        reduces the list's size by 1
        """
        
        stepCount = 0

        currentNode = self.head

        while stepCount < self.size():
            if stepCount == index:
                prvNode = currentNode.previousNode
                nxtNode = currentNode.nextNode
                
                currentNode.nextNode = None
                currentNode.previousNode = None
                
                if prvNode == None:
                    self.head = nxtNode
                else:
                    prvNode.nextNode = nxtNode

                if nxtNode == None:
                    self.tail = prvNode
                else:
                    nxtNode.previousNode = prvNode

                self.count -=1
                return
            else:
                currentNode = currentNode.nextNode
                stepCount += 1

    def insertItem(self, data, index: int) -> None:
        pass

#the end