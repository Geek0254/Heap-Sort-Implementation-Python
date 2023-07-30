# Heap-Sort Implementation In Python
This repository contains a Python implementation of the Heap Sort algorithm. Heap Sort is a comparison-based sorting algorithm that leverages the properties of a max-heap data structure to efficiently sort an array in ascending order.

# Introduction
Heap Sort is an efficient sorting algorithm with a time complexity of O(n log n). It works by first transforming the input array into a max-heap data structure and then repeatedly extracting the maximum element from the heap to build the sorted array.

# key components of this repository 
'heapify' function to convert an array into a max-heap.
'heap_sort' function to perform Heap Sort on an array.
A main function that demonstrates the usage of the heapify and heap_sort functions.
Random array initialization functionality to test the algorithm with different input sizes and values.

# Usage
Clone this repository to your local machine using git clone.
Navigate to the repository's directory.
Run the Python script heap_sort.py using python heap_sort.py.
Enter the size of the array (The script generate random values for you).
The script will display the array before heapifying, after heapifying, and after heap sort. It will also show the time taken for both heapifying and heap sort operations.

# Algorithm
The heapify function is used to convert an array into a max-heap data structure.
Starting from the last non-leaf node, the heapify function is called repeatedly to build the max heap.
The heap_sort function extracts the maximum element from the heap, swaps it with the last element in the unsorted part of the array, and then calls heapify on the reduced heap size.
The heap_sort function repeats this process until the entire array is sorted.

# Performance
The Heap Sort algorithm has a time complexity of O(n log n), making it efficient for large datasets. It uses in-place sorting, which means it requires no additional memory allocation beyond the original array. However, Heap Sort is not a stable sorting algorithm.
To verify the algorithm's performance, the script provides the time taken for both heapifying and heap sort operations on the given array. It also demonstrates how the algorithm works on arrays with varying sizes and values.
