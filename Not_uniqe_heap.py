'''

  Task: The way to create a heap from the set of the elements is not unique. For example, [1, 2, 3] and [1, 3, 2] are both valid min heaps. Though there are much more possible heaps, your task is to show that there could be two different one.

'''
def unique_heap(arr):
    arr = sorted(arr)
    new_arr = arr.copy()

    if len(arr) > 2:
        new_arr[1], new_arr[2] = new_arr[2], new_arr[1]

    result = ''
    for el in arr:
        result += str(el)+ ' '

    result = result.strip() + '\n'

    for el in new_arr:
        result += str(el) + ' '

    return result.strip()



inp = open('input.txt', 'r')
out = open('output.txt', 'w')
out.write(unique_heap(list(map(int, list(inp.readline().split(' ')))))) 
inp.close()
