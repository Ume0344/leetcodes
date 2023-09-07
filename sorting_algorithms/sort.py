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

        if l <= 1:
            return array

        for i in range(l-1):
            for j in range(i+1, l):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]

        return array
    
    def quick_sort(self, array: list) -> list:
        """
        Sort the array through quick sort algorithm.
        It finds the pivot(middle point in array). create 3 arrays (left, right, middle). loop over whole array
        If element in array is smaller than pivot, put it in left, greater put it in right and if not put it in middle
        Now, do recursion on sub-arrays (left, right). At the end, combine them
        param array: List of numbers to be sorted.
        return array: Sorted list of numbers.
        """

        # [2,3,1,5,4]
        # first iteration: left = [], right = [2,3,5,4] middle = [1] -> [1,2,3,4,5]
        # second iteration: left = [], left1 = [2,3,4], right1 = [], middle1 = [5] -> [2,3,4,5]
        # third iteration: left2 = [2], right2 = [4], middle = [3] -> [2,3,4]

        l = len(array)

        if l <= 1:
            return array

        pivot = l // 2

        left, right, middle = [], [], []

        for i in range(l):
            if array[i] < array[pivot]:
                left.append(array[i])
            elif array[i] > array[pivot]:
                right.append(array[i])
            else:
                middle.append(array[i])

        left = self.quick_sort(left)
        right = self.quick_sort(right)

        return left + middle + right
