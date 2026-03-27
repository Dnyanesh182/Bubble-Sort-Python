# UC4 – Count number of comparisons and swaps performed during sorting

from typing import List, Tuple


class BubbleSort:
    """Class to implement Bubble Sort with metrics tracking."""

    @staticmethod
    def sort(data: List[int]) -> Tuple[List[int], int, int]:
        """
        Sorts a list and counts comparisons and swaps.

        :param data: List of integers
        :return: Tuple of (sorted list, comparisons, swaps)
        """
        n: int = len(data)
        comparisons: int = 0
        swaps: int = 0

        if n <= 1:
            return data, comparisons, swaps

        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1

                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1

        return data, comparisons, swaps


def main() -> None:
    """Main execution function."""
    data: List[int] = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", data)

    sorted_data, comparisons, swaps = BubbleSort.sort(data.copy())

    print("Sorted List:", sorted_data)
    print("Total Comparisons:", comparisons)
    print("Total Swaps:", swaps)


if __name__ == "__main__":
    main()