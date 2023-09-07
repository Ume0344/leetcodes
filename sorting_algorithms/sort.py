class Sort:
    def __init__(self) -> None:
        pass

    def bubble_sort(self, array: list) -> list:
        """
        Sort the array through bubble sort algorithm.
        param array: List of numbers to be sorted.
        return array: Sorted list of numbers.
        """
        l = len(array)

        for i in range(l-1):
            for j in range(i+1, l):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]

        print(array)
        return array
