# 求一个无序数组中 最小的k个。
# 方法：维持一个size 为k 的 大顶堆， 非递归
# 时间复杂度 nlogk


def heapify(heap, index, heapsize):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    while left < heapsize:
        if heap[left] > heap[largest]:
            largest = left
        if right < heapsize and heap[largest] < heap[right]:
            largest = right
        if largest != index:
            swap(heap, largest, index)
        else:
            break
        index = largest
        left = index * 2 + 1
        right = index * 2 + 2
    return heap


def swap(heap, parent, index):
    heap[parent], heap[index] = heap[index], heap[parent]


def heapInsert(heap, value, index):
    heap.insert(index, value)
    while index != 0:
        parent = (index - 1) // 2
        if heap[parent] < heap[index]:
            swap(heap, parent, index)
            index = parent
        else:
            break
    print(heap)


def getMinKnumbersByheap(arr, k):
    # 创建堆
    l = arr[:]
    heap = []
    for i in range(k):
        heapInsert(heap, l[i], i)
    for i in range(k, len(arr)):
        if heap[0] > l[i]:
            heap[0] = l[i]
            heapify(heap, 0, k)
    return heap


def getMinKnums(arr, k):
    import heapq
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])
    for i in range(k, len(arr)):
        heapq.heappushpop(heap, arr[i])
    return heap


if __name__ == '__main__':
    l = [9, 4, 8, 3, 1, 2, 5]
    print(l)
    res = getMinKnums(l, 4)
    print(res)


