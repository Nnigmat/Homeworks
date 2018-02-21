import sys


def hidden_merge(arr1, arr2):
    """
        Function merge is return [] if length of arrays is equal 0
        Otherwise it take minimal element in all arrays and return it and new array without this element
        :param arrays:
        11:return:
        """
    count = len(arr1) + len(arr2)

    res = []

    while count > 0:
        if len(arr1) != 0 and len(arr2) != 0:
            if arr1[0] < arr2[0]:
                  res.append(arr1.pop(0))
            else:
                res.append(arr2.pop(0))
        elif len(arr1) == 0:
            while count > 0:
                res.append(arr2.pop(0))
                count -= 1

        else:
            while count > 0:
                res.append(arr1.pop(0))
                count -= 1

        count -= 1

    return [res]

def merge(arrays):

    if len(arrays) <= 1:
        return arrays[0]
    else:
        i = 0
        while i < len(arrays):
            if i+1 != len(arrays):
                arrays = hidden_merge(arrays[i], arrays[i+1]) + arrays
                arrays.pop(i+1)
                arrays.pop(i+1)
            i+=1
        return merge(arrays)


sys.setrecursionlimit(100000000)

# Variables for reading and writing
inp = open("input.txt", 'r')
out = open("output.txt", 'w')

# Read number of arrays
n_of_arrays = int(inp.readline())

# Parsing array of arrays
arrays = []
while n_of_arrays > 0:
    arr = inp.readline().strip().split(" ")
    if arr[0] != '':
        arr = list(map(int, arr))
        arrays.append(arr)
    n_of_arrays -= 1
inp.close()

# Output of program
for el in merge(arrays):
    out.write(''.join(str(el) + " "))
out.close()
