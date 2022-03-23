class MergeSort(object):
    """docstring for MergeSort"""
    def __init__(self, numbers):
        self.numbers = numbers
        self.count = len(numbers)

    def sort(self):
        """docstring for sort"""
        self.merge_sort(0, self.count - 1)
        return self.numbers

    def merge_sort(self, low, high):
        """docstring for merge_sort"""
        if low < high:
            mid = (low + high) // 2

            # Divide
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        """docstring for merge"""
        b = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.numbers[i] <= self.numbers[j]:
                b.append(self.numbers[i])
                i += 1
            else:
                b.append(self.numbers[j])
                j += 1

        while i <= mid:
            b.append(self.numbers[i])
            i += 1

        while j <= high:
            b.append(self.numbers[j])
            j += 1

        for index, value in enumerate(b):
            self.numbers[low + index] = value
