# Sorting Benchmark Lab
## Analysis of Algorithms Project

### 1. Introduction

Sorting is an important operation in computer science. It is used to arrange data in a specific order, such as ascending or descending order.

In this project, we compare four sorting methods:
- Insertion Sort
- Merge Sort
- Quick Sort
- Python Built-in Sort (`sorted()`)

The main goal is to study how these algorithms work and compare their execution times with different input sizes and data types.

### 2. Algorithms and Time Complexity

**Insertion Sort**

Insertion Sort builds the sorted list one element at a time. It is simple and works well with small or already sorted data.

- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

**Merge Sort**

Merge Sort divides the list into smaller parts, sorts them, and combines the results.

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Quick Sort**

Quick Sort selects a pivot element and divides the list into smaller and larger elements. In this project, the last element is used as the pivot.

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

**Python Built-in Sort**

Python provides a built-in sorting function called `sorted()`. It uses Timsort, which works efficiently with different types of data.

- Best Case: O(n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

### 3. Experimental Method

The project was implemented using Python.

We tested the algorithms using three types of input data:
- Sorted Data: Elements are already arranged.
- Reversed Data: Elements are arranged in descending order.
- Random Data: Elements are in random order.

We used different input sizes, from 1,000 to 100,000 elements.

The execution time was measured using Python's `time.perf_counter()` function.

We also used:
- CSV files to save the experimental results.
- Matplotlib to create comparison charts.
- Unit tests to check the correctness of the algorithms.

To avoid very long execution times, Insertion Sort was tested up to 5,000 elements. Quick Sort with sorted and reversed inputs was also limited to 5,000 elements because using the last element as a pivot can lead to O(n²) time complexity.

### 4. Results and Discussion

The experiment helps us understand how input data affects sorting performance.

**Insertion Sort:** It performs well with small or already sorted lists, but its execution time increases quickly with large inputs.

**Merge Sort:** It provides consistent performance because its time complexity is O(n log n) in all cases.

**Quick Sort:** It can be fast with random data. However, choosing the last element as the pivot can make it slow with sorted or reversed data.

**Python Built-in Sort:** It is expected to perform efficiently because Python uses the optimized Timsort algorithm.

The generated charts show the execution time of each algorithm for different input sizes and data types. The CSV file contains the measured execution times.

### 5. Conclusion

In this project, we implemented and compared four sorting algorithms using Python.

The experiment shows that different algorithms have different performance depending on the input size and data arrangement. Insertion Sort is suitable for small datasets. Merge Sort provides stable performance. Quick Sort can be efficient with random data but may become slow with a poor pivot choice. Python's built-in sorting function provides an efficient general-purpose solution.

This project helped us understand the relationship between time complexity and actual execution time.

### 6. Future Work

In the future, we can improve this project by:
- Testing larger datasets.
- Trying different pivot selection methods in Quick Sort.
- Comparing more sorting algorithms.
- Repeating experiments and calculating average execution times.
