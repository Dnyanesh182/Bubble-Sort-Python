# UC7 – Sort custom objects using Bubble Sort with key (e.g., sort by age)

from typing import List, Callable, TypeVar

T = TypeVar("T")


class Person:
    """Represents a person with name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"({self.name}, {self.age})"


class BubbleSort:
    """Class to implement Bubble Sort for custom objects."""

    @staticmethod
    def sort(data: List[T], key: Callable[[T], int]) -> List[T]:
        """
        Sorts a list of objects based on a key function.

        :param data: List of objects
        :param key: Function to extract comparison key
        :return: Sorted list
        """
        n: int = len(data)

        if n <= 1:
            return data

        for i in range(n):
            for j in range(0, n - i - 1):
                if key(data[j]) > key(data[j + 1]):
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data


def main() -> None:
    """Main execution function."""
    people: List[Person] = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 30),
        Person("David", 20),
    ]

    print("Original List:", people)

    sorted_people: List[Person] = BubbleSort.sort(
        people.copy(), key=lambda person: person.age
    )

    print("Sorted List (by age):", sorted_people)


if __name__ == "__main__":
    main()