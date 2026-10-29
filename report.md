# Empirical Analysis of Insertion Sort

## Method
Insertion sort was tested with 100, 500, 1,000, 2,000, 3,000, 4,000 and 5,000 numbers. Three inputs were used: sorted, reverse-sorted and random. The program counted comparisons and shifts and measured running time.

## Results
Sorted input was the fastest because it needed almost no shifts. Reverse-sorted input was the slowest because each new number had to move past the previous numbers. Random input was between these cases. The graph shows how the running time changes as the input size increases. Exact times depend on the computer used.

## Complexity and Merge Sort
Insertion sort takes about O(n) time for already sorted input, but O(n²) time for reverse-sorted and average random input. Merge sort takes O(n log n) time, so it is usually better for large inputs. Insertion sort is simple and can work well for small or nearly sorted lists.
