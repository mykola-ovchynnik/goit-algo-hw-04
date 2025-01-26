import random
import timeit
import pandas as pd


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# compare performance
def compare_sorting_algorithms():
    sizes = [100, 1000, 10000]
    results = []

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        data_merge = data[:]
        data_insertion = data[:]
        data_sorted = data[:]

        merge_time = timeit.timeit(lambda: merge_sort(data_merge), number=1)

        insertion_time = timeit.timeit(lambda: insertion_sort(data_insertion), number=1)

        sorted_time = timeit.timeit(lambda: sorted(data_sorted), number=1)

        results.append(
            {
                "Size": size,
                "Merge Sort": merge_time,
                "Insertion Sort": insertion_time,
                "Timsort": sorted_time,
            }
        )

    return results


results = compare_sorting_algorithms()

df = pd.DataFrame(results)
print("Sorting Algorithms Performance Comparison")
print(df)

# Емпіричний аналіз підтверджує, що Timsort, який поєднує сортування злиттям та сортування вставками,
# є значно ефективнішим для даних наборів.
