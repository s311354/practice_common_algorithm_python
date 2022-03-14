from quick_sort import QuickSort


def contain_same_ints(arr1, arr2):
    """docstring for contain_same_intsa"""
    for i in arr1:
        found = False
        for j in arr2:
            if i == j:
                found = True
            if not found:
                return False

    return True


def is_sorted(numbers):
    """docstring for is_sorted"""
    last_num = float("-inf")

    for num in numbers:
        if num < last_num:
            return False
        else:
            last_num = num
    return True


def check_sort(original):
    """docstring for check_sort"""
    numbers = original[:]
    qs = QuickSort(numbers)

    output = qs.sort()

    print(output)

    if is_sorted(output):
        print("*** SUCESS! ***")
    else:
        print("Uh oh - not inn order")

    if contain_same_ints(original, numbers):
        print("** Contain the same elements! **")
    else:
        print("Uh oh - something is missing.")

    print("----")


def main():
    """docstring for fname"""
    check_sort([325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221])

    check_sort([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])

    check_sort([3, 5, 7, 9, 23, 25, 34, 53, 77, 199])

    check_sort([3, 5, 7])
    check_sort([3, 5])
    check_sort([3])


if __name__ == "__main__":
    main()
