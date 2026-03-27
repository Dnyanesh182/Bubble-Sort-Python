# UC1 – Implement basic Bubble Sort to sort an array in ascending order

from typing import List


class BubbleSort:
    """Class to implement basic Bubble Sort."""

    @staticmethod
    def sort(data: List[int]) -> List[int]:
        """
        Sorts a list in ascending order using Bubble Sort.

        :param data: List of integers
        :return: Sorted list
        """
        n: int = len(data)

        if n <= 1:
            return data

        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data


def main() -> None:
    """Main execution function."""
    data: List[int] = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", data)
    sorted_data: List[int] = BubbleSort.sort(data.copy())
    print("Sorted List:", sorted_data)


if __name__ == "__main__":
    main()