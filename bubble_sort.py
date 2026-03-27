# UC3 – Optimize Bubble Sort using early exit flag to improve performance

from typing import List


class BubbleSort:
    """Class to implement optimized Bubble Sort."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts a list in ascending order using optimized Bubble Sort.

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


def main() -> None:
    """Main execution function."""
    data: List[int] = [11, 12, 22, 25, 34, 64, 90]

    print("Original List:", data)
    sorted_data: List[int] = BubbleSort.sort(data.copy())
    print("Sorted List:", sorted_data)


if __name__ == "__main__":
    main()