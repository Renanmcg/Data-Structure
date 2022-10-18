# Max Heap
class Maxheap:
    def __init__(self, items = []):
        super().__init__()
        self.heap=[0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self,data):

        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):

        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):

        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubble.Down(1)
        elif len(self.heap) == 2:
            max = self.hrap.pop()
        else:
            max = false
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)

# Min Heap
class Minheap:
    def __init__(self, items = []):
        super().__init__()
        self.heap=[0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self,data):

        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):

        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):

        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            min = self.heap.pop()
            self.__bubble.Down(1)
        elif len(self.heap) == 2:
            min = self.hrap.pop()
        else:
            min = false
        return min

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.__bubbleDown(smallest)

    def __str__(self):
        return str(self.heap)