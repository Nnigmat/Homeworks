'''
  Task: The standard implementation of quicksort algorithm contains two recursive calls to itself - after partition is called, left subarray and right subarray are recursively sorted. The second recursive call in quicksort is not really necessary; we can avoid it by using an iterative control structure. This technique, called tail recursion, is provided automatically by good compilers. Consider the following version of quicksort, which simulates tail recursion:

TAIL-RECURSIVE-QUICKSORT(A, p, r)
     while p < r
          // Partition and sort left subarray.
          q = PARTITION(A, p, r)
          TAIL-RECURSIVE-QUICKSORT(A, p, q-1)
          p = q + 1
Compilers usually execute recursive procedures by using a stack that contains pertinent information, including the parameter values, for each recursive call. The information for the most recent call is at the top of the stack, and the information for the initial call is at the bottom. Upon calling a procedure, its information is pushed onto the stack; when it terminates, its information is popped. Since we assume that array parameters are represented by pointers, the information for each procedure call on the stack requires  stack space. The stack depth is the maximum amount of stack space used at any time during a computation.

Think when the above-mentioned algorithm’s stack depth is  on an n-element input array. Modify the code for TAIL-RECURSIVE-QUICKSORT so that the worst-case stack depth is . Maintain the  expected running time of the algorithm.

Implement the modified version of TAIL-RECURSIVE-QUICKSORT
'''

def balancing(arr, left, right):
    # Choose the most right element with which we will
    # compare other elements
    el = arr[right]

    counter = left - 1

    # Goes for every element in array from left to right indexes
    for i in range(left, right):
        if el >= arr[i]:
            counter = counter + 1

            # Swap elements with each other
            temp = arr[counter]
            arr[counter] = arr[i]
            arr[i] = temp

    temp = arr[counter+1]
    arr[counter+1] = arr[right]
    arr[right] = temp
    return counter


def quick_sort_by_tail_recursion(arr, left, right):
    while right > left:
        pivot = balancing(arr, left, right)
        quick_sort_by_tail_recursion(arr, left, pivot)
        left = pivot + 2
    return arr
inp = open('input.txt', 'r')
out = open('output.txt', 'w')
arr_temp = list(map(int, inp.readline().strip().split(' ')))
out.write(' '.join(list(map(str, (quick_sort_by_tail_recursion(arr_temp, 0, len(arr_temp)-1))))))
inp.close()
