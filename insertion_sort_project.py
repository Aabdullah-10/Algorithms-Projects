import random
import time
import matplotlib.pyplot as plt


def insertion_sort(a):
    a = a.copy()
    comparisons = 0
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons, shifts


sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
types = ['Sorted', 'Reverse', 'Random']
results = []

for n in sizes:
    for kind in types:
        if kind == 'Sorted':
            data = list(range(n))
        elif kind == 'Reverse':
            data = list(range(n, 0, -1))
        else:
            data = list(range(n))
            random.shuffle(data)
        start = time.perf_counter()
        sorted_data, comparisons, shifts = insertion_sort(data)
        elapsed = (time.perf_counter() - start) * 1000
        results.append([n, kind, round(elapsed, 4), comparisons, shifts])
        assert sorted_data == sorted(data)
        print(n, kind, round(elapsed, 4), comparisons, shifts)



plt.figure(figsize=(8, 5))
for kind in types:
    rows = [r for r in results if r[1] == kind]
    plt.plot([r[0] for r in rows], [r[2] for r in rows], marker='o', label=kind)
plt.xlabel('Number of elements (n)')
plt.ylabel('Running time (milliseconds)')
plt.title('Insertion Sort Running Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show

