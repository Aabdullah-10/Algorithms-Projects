# Insertion Sort

 Method
I wrote an insertion sort program in Python. I tested it with 100, 500, 1000, 2000, 3000, 4000 and 5000 numbers. I used sorted, reverse-sorted and random numbers. I also counted the comparisons and shifts and measured the running time.

 Results
The results showed that insertion sort was fastest with sorted numbers because it did not need to move many elements. Reverse-sorted numbers took the longest time because the program had to move many elements. Random numbers were between the two cases. The running time increased as the number of elements increased, especially for reverse-sorted input.

Insertion sort is simple and works well with small or already sorted lists. Its time complexity is O(n) for sorted input and O(n²) for reverse-sorted and average random input. Merge sort is usually faster for large lists because its time complexity is O(n log n). Therefore, merge sort is a better choice for large amounts of data.