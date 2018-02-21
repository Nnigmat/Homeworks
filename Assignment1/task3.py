import random


def randomize_in_place(arr):
    """
    'randomize_in_place' method randomly swaps the element of income array
    It use numpy  library for generation random integer
    :param arr:
    :return:
    """

    # Goes for each element in array
    for i in range(len(arr)):
        # Gets random integer index with which we need to swap current element
        n = random.randint(i, len(arr) - 1)

        # Swaps elements with each other
        arr[n], arr[i] = arr[i], arr[n]


def select(arr, k):
    """
    This method return K'th largest element in array using randomization on it
    :param arr:
    :param k:
    :return:
    """

    # Firstly, randomize income array using "randomize_in_place" method
    randomize_in_place(arr)

    arr = sorted(arr)

    # Return k'th element in largest array
    return arr[len(arr) - k]


f = open('input.txt', 'r')
k = int(f.readline().strip())

arr = list(map(int, f.readline().strip().split(' ')))
f.close()

f = open('output.txt', 'w')
f.write(str(select(arr, k)))
