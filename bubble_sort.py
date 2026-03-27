# UC6 – Apply Bubble Sort on list of strings using lexicographical order

from typing import List


class BubbleSort:
    """Class to implement Bubble Sort for strings."""

    @staticmethod
    def sort(data: List[str]) -> List[str]:
        """
        Sorts a list of strings lexicographically.

        :param data: List of strings
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
    data: List[str] = ["banana", "apple", "cherry", "date"]

    print("Original List:", data)
    sorted_data: List[str] = BubbleSort.sort(data.copy())
    print("Sorted List:", sorted_data)


if __name__ == "__main__":
    main()