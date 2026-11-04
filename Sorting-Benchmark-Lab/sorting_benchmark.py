import random
import time
import csv
import os
import unittest
import matplotlib.pyplot as plt


def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    arr = arr.copy()
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            pivot_index = i + 1
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))

            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

    return arr


def python_sort(arr):
    return sorted(arr)


def generate_data(size, data_type):
    if data_type == "sorted":
        return list(range(size))

    if data_type == "reversed":
        return list(range(size, 0, -1))

    return [random.randint(0, size * 10) for _ in range(size)]


def measure_time(sort_function, data):
    start = time.perf_counter()
    result = sort_function(data)
    end = time.perf_counter()

    if result != sorted(data):
        raise ValueError("Incorrect sorting result")

    return end - start


sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000]

data_types = ["sorted", "reversed", "random"]

algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Python sorted()": python_sort
}


def run_benchmark():
    results = []

    for data_type in data_types:
        print("\nTesting:", data_type)

        for size in sizes:
            data = generate_data(size, data_type)

            for name, algorithm in algorithms.items():

                if name == "Insertion Sort" and size > 5000:
                    continue

                if name == "Quick Sort" and data_type != "random" and size > 5000:
                    continue

                execution_time = measure_time(algorithm, data)

                results.append({
                    "Algorithm": name,
                    "Data Type": data_type,
                    "Input Size": size,
                    "Execution Time": execution_time
                })

                print(name, size, execution_time)

    return results


def save_results(results):
    os.makedirs("benchmark_results", exist_ok=True)

    with open("benchmark_results/results.csv", "w", newline="") as file:
        fields = [
            "Algorithm",
            "Data Type",
            "Input Size",
            "Execution Time"
        ]

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)


def plot_results(results):
    os.makedirs("benchmark_results", exist_ok=True)

    for data_type in data_types:
        plt.figure(figsize=(9, 5))

        for name in algorithms:
            data = [
                row for row in results
                if row["Algorithm"] == name
                and row["Data Type"] == data_type
            ]

            if data:
                x = [row["Input Size"] for row in data]
                y = [row["Execution Time"] for row in data]

                plt.plot(x, y, marker="o", label=name)

        plt.title(data_type.capitalize() + " Data")
        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (seconds)")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(f"benchmark_results/{data_type}.png")
        plt.close()


class TestSorting(unittest.TestCase):

    def test_algorithms(self):
        test_cases = [
            [],
            [5],
            [4, 2, 4, 1, 2, 3],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [-5, 3, -1, 0, 8]
        ]

        for algorithm in algorithms.values():
            for data in test_cases:
                self.assertEqual(algorithm(data), sorted(data))


if __name__ == "__main__":
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(TestSorting)
    test_result = unittest.TextTestRunner().run(tests)

    if not test_result.wasSuccessful():
        raise SystemExit("Tests failed")

    results = run_benchmark()
    save_results(results)
    plot_results(results)

    print("\nBenchmark completed successfully!")
