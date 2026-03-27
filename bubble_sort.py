# UC5 – Handle sorting of duplicate elements correctly while maintaining stability

from typing import List, Tuple


class BubbleSort:
    """Class to implement stable Bubble Sort."""

    @staticmethod
    def sort(data: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
        """
        Sorts list of tuples based on first element while maintaining stability.

        :param data: List of tuples (value, identifier)
        :return: Sorted list preserving order of duplicates
        """
        n: int = len(data)

        if n <= 1:
            return data

        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare only values (first element)
                if data[j][0] > data[j + 1][0]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data


def main() -> None:
    """Main execution function."""
    data: List[Tuple[int, str]] = [
        (5, "A"),
        (3, "B"),
        (5, "C"),
        (2, "D"),
        (3, "E"),
    ]

    print("Original List:", data)

    sorted_data: List[Tuple[int, str]] = BubbleSort.sort(data.copy())

    print("Sorted List (Stable):", sorted_data)


if __name__ == "__main__":
    main()