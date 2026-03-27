# UC10 – Refactor Bubble Sort implementation using clean code practices and reusable functions

from typing import List, TypeVar, Callable, Optional

T = TypeVar("T")


class BubbleSort:
    """Refactored Bubble Sort with reusable and generic design."""

    @staticmethod
    def sort(
        data: List[T],
        key: Optional[Callable[[T], int]] = None,
        reverse: bool = False,
    ) -> List[T]:
        """
        Generic Bubble Sort implementation.

        :param data: List of elements
        :param key: Optional key function for custom sorting
        :param reverse: Sort in descending order if True
        :return: Sorted list
        """
        n: int = len(data)

        if n <= 1:
            return data

        key_func: Callable[[T], int] = key if key else lambda x: x

        for i in range(n):
            swapped: bool = False

            for j in range(0, n - i - 1):
                left = key_func(data[j])
                right = key_func(data[j + 1])

                should_swap: bool = (
                    left > right if not reverse else left < right
                )

                if should_swap:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True

            if not swapped:
                break

        return data


def main() -> None:
    """Main execution function."""
    data: List[int] = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", data)

    asc_sorted = BubbleSort.sort(data.copy())
    desc_sorted = BubbleSort.sort(data.copy(), reverse=True)

    print("Ascending:", asc_sorted)
    print("Descending:", desc_sorted)


if __name__ == "__main__":
    main()