#  implement heap in python with convert list to heap, insert, delete, heapify, heap_sort

class MinHeap:
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(arr)
    
    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < self.heap_size and self.arr[left] < self.arr[i]:
            smallest = left
        if right < self.heap_size and self.arr[right] < self.arr[smallest]:
            smallest = right
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.heapify(smallest)