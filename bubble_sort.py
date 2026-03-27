# UC9 – Compare Bubble Sort performance with Selection Sort

from typing import List
import time
import random


class BubbleSort:
    """Optimized Bubble Sort implementation."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        n: int = len(data)
        for i in range(n):
            swapped: bool = False
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break
        return data


class SelectionSort:
    """Selection Sort implementation."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        n: int = len(data)
        for i in range(n):
            min_index: int = i
            for j in range(i + 1, n):
                if data[j] < data[min_index]:
                    min_index = j
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
        return data


def compare_performance(size: int) -> None:
    """Compare execution time of Bubble Sort and Selection Sort."""
    data: List[int] = [random.randint(1, 1000) for _ in range(size)]

    # Bubble Sort
    start_time: float = time.time()
    BubbleSort.sort(data.copy())
    bubble_time: float = time.time() - start_time

    # Selection Sort
    start_time = time.time()
    SelectionSort.sort(data.copy())
    selection_time: float = time.time() - start_time

    print(f"Input Size: {size}")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Selection Sort Time: {selection_time:.6f} seconds")
    print("-" * 40)


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [100, 500, 1000]

    print("Performance Comparison: Bubble Sort vs Selection Sort")
    for size in sizes:
        compare_performance(size)


if __name__ == "__main__":
    main()