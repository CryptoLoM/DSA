import random
import time

def generate_random_array(length):
    return [random.randint(0, 10000) for _ in range(length)]

def ShellSort(arr):
    n = len(arr)
    comparisons = 0
    exchanges = 0
    start_time = time.time()

    gap = n // 2
    swapped = True  # Show, that list isn't sorted

    while gap > 0 and swapped:  # Continue sorting, while is exchange and unsorted list
        swapped = False  # Assume, that the list is sorted on this iteration
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparisons += 1  # Counting of compares
                exchanges += 1   # Counting of exchanges
                swapped = True   # If there is an exchange, we indicate that the list is not sorted
            arr[j] = temp

        gap //= 2

    execution_time = time.time() - start_time
    return comparisons, exchanges, execution_time

array_lengths = [100, 1000, 10000]

for length in array_lengths:
    total_comparisons = 0
    total_exchanges = 0
    total_execution_time = 0

    for _ in range(10):
        arr = generate_random_array(length)
        comparisons, exchanges, execution_time = ShellSort(arr.copy())
        total_comparisons += comparisons
        total_exchanges += exchanges
        total_execution_time += execution_time

    comparisons_avg = total_comparisons / 10
    exchanges_avg = total_exchanges / 10
    execution_time_avg = total_execution_time / 10

    arr = generate_random_array(length)
    print(f'Unsorted array with {length} elements:', arr)
    comparisons, exchanges, execution_time = ShellSort(arr.copy())
    print(f'Number of comparisons: {comparisons}')
    print(f'Number of exchanges: {exchanges}')
    print(f'Execution time: {execution_time} seconds')

    print("Sorted array:")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" ")
    print("\n")
