'''
 Task: Write a program that takes as input N English words written in lower case, and sort them in lexicographic order. For example, if the input is

blue red green

then the output should be

blue green red

As another example, if the input is

apples apple

then the output should be

apple apples

Implement your program by using the radix sort. Note that there are 26 lower-case letters in English. As shown in the example, the lengths of the words can be different from each other.
'''
def radix_sort(arr):
    max_length = -1
    for el in arr:
        if len(el) > max_length:
            max_length = len(el)

    for i in range(len(arr)):
        arr[i] = arr[i] + ' ' * (max_length - len(arr[i]))

    for i in range(max_length - 1, -1, -1):
        count = [[] for _ in range(27)]
        delta = 96

        for el in arr:
            if el[i] != ' ':
                count[ord(el[i]) - delta].append(el)
            else:
                count[0].append(el)

        arr = []
        for array in count:
            for el in array:
                arr.append(el)

    return [el.strip() for el in arr]


inp = open('input.txt', 'r')
out = open('output.txt', 'w')
out.write(' '.join(radix_sort(list(inp.readline().split(' ')))))
inp.close()
