# UC8 – Analyze time complexity of Bubble Sort with different input sizes

from typing import List
import time
import random


class BubbleSort:
    """Class to implement optimized Bubble Sort."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts a list using optimized Bubble Sort.

        :param data: List of integers
        :return: Sorted list
        """
        n: int = len(data)

        if n <= 1:
            return data

        for i in range(n):
            swapped: bool = False
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break

        return data


def analyze_performance(sizes: List[int]) -> None:
    """Analyzes execution time for different input sizes."""
    for size in sizes:
        data: List[int] = [random.randint(1, 1000) for _ in range(size)]

        start_time: float = time.time()
        BubbleSort.sort(data.copy())
        end_time: float = time.time()

        print(f"Input Size: {size}, Time Taken: {end_time - start_time:.6f} seconds")


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [10, 100, 500, 1000]

    print("Bubble Sort Time Complexity Analysis:")
    analyze_performance(sizes)


if __name__ == "__main__":
    main()