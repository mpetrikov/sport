import math1

def heap_add(heap, element):
    heap.append(element)

    i = len(heap) - 1

    parent = int((i-1) / 2)

    while i > 0 and heap[parent] < heap[i]:
        temp = heap[i]
        heap[i] = heap[parent]
        heap[parent] = temp

        i = parent
        parent = int((i - 1) / 2)

def heapify_from_position(heap, i):
    heapSize = len(heap)

    while True:
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largestChild = i

        if leftChild < heapSize and heap[leftChild] > heap[largestChild]:
            largestChild = leftChild

        if rightChild < heapSize and heap[rightChild] > heap[largestChild]:
            largestChild = rightChild

        if largestChild == i:
            break

        temp = heap[i]
        heap[i] = heap[largestChild]
        heap[largestChild] = temp
        i = largestChild

def heap_remove(heap, value):
    position = heap.index(value)
    heap[position] = heap[-1]
    del heap[-1]

    if position == 0:
        child1Position = 1
        child2Position = 2
    else:
        child1Position = 2 * position + 1
        child2Position = 2 * position + 2
    heap_length = len(heap)

    while child1Position < heap_length or child2Position < heap_length:
        if child1Position < heap_length and child2Position < heap_length:
            if heap[position] < heap[child1Position] and heap[position] < heap[child2Position]:
                break
            else:
                # спускаем вниз значение, если у удаляемого узла 2 потомка
                if heap[child1Position] < heap[child2Position]:
                    temp = heap[position]
                    heap[position] = heap[child1Position]
                    heap[child1Position] = temp

                    position = child1Position
                else:
                    temp = heap[position]
                    heap[position] = heap[child2Position]
                    heap[child2Position] = temp

                    position = child2Position
        else: # heap[position] имеет строго одного потомка
            if heap[position] < heap[child1Position]:
                break
            else:
                temp = heap[position]
                heap[position] = heap[child1Position]
                heap[child1Position] = temp

                position = child1Position

        child1Position = 2 * position + 1
        child2Position = 2 * position + 2
