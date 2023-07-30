import random
import time

def heapify(array, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, heap_size)

def heap_sort(array):
    heap_size = len(array)

    for i in range(heap_size // 2 - 1, -1, -1):  # Start from the last non-leaf node
        heapify(array, i, heap_size)

    for i in range(heap_size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)


def main():
    array_size = int(input("Enter the array size: "))
    array = [random.randint(1, 100) for _ in range(array_size)]  # Initialize with random values

    print("The array before heapifying: ", array[:])  # [:] Create a copy of the original array
    start_time = time.time()
    heapify(array, 0, array_size)
    end_time = time.time()
    print("The array after heapifying: ", array)

    heap_sort_array = array[:]  # Create a copy of the array for heap sort
    start_time_sort = time.time()
    heap_sort(heap_sort_array)
    end_time_sort = time.time()
    print("The array after heap sort: ", heap_sort_array)

    print("Time taken for heapifying: ", end_time - start_time, "seconds")
    print("Time taken for heap sort: ", end_time_sort - start_time_sort, "seconds")


if __name__ == "__main__":
    main()
