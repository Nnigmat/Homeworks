def maxCrossingArray(arr, left, mid, right):
    '''
    "maxCrossingArray" method searches maximum subarray in intersection of two arrays
    :param arr:
    :param left:
    :param mid:
    :param right:
    :return:
    '''

    # Search max sum of prefix
    leftSum = -9999999
    summa = 0
    maxLeft = 0
    i = mid
    while i >= left:
        summa += arr[i]
        if summa > leftSum:
            leftSum = summa
            maxLeft = i
        i-=1

    # Search max sum of postfix
    rightSum = -9999999
    summa = 0
    maxRight = 0
    i = mid+1
    while i <= right:
        summa += arr[i]
        if summa > rightSum:
            rightSum = summa
            maxRight = i
        i+=1

    # Combine two results and return it
    maxSum = leftSum+rightSum
    return [maxLeft, maxRight, maxSum]

def maxSubarrayHided(arr, left, right):
    '''
    "maxSubarrayHided" method search the maximum subarray in given array, using divide
    and conquer approach
    :param arr:
    :param left:
    :param right:
    :return:
    '''

    # If we get array with 1 element return it
    if left == right:
        return [left, right, arr[left]]

    # Otherwise divide array in two subarrays, use "maxSubarrayHided" on them,
    # after check crossing array and combine them
    else:
        # Index of middle element
        mid = int((left+right)/2)

        # Use "maxSubarrayHided" on parts of array
        left_arr = maxSubarrayHided(arr, left, mid)
        right_arr = maxSubarrayHided(arr, mid+1, right)

        # Find maximum subarray in intersection of two parts of array
        crossing_arr = maxCrossingArray(arr, left, mid, right)

        # Combining them and returning the "*_arr" with the highest sum
        if left_arr[2] >= right_arr[2] and left_arr[2] >= crossing_arr[2]:
            return left_arr
        elif left_arr[2] <= right_arr[2] and right_arr[2] >= crossing_arr[2]:
            return right_arr
        else:
            return crossing_arr


def maxSubarray(arr):
    '''
    "maxSubarray" method start "maxSubarrayHided" method which gets some additional
    arguments

    After it gets result and return it to user
    :param arr:
    :return:
    '''
    res = maxSubarrayHided(arr, 0, len(arr)-1)
    return [res[2], arr[res[0]:res[1]+1]]

f = open('input.txt', 'r')
res = maxSubarray(list(map(int, f.readline().strip().split(' '))))
f.close()
f = open('output.txt', 'w')
f.write(str(res[0])+'\n')
for el in res[1]:
    f.write(str(el)+" ")

f.close()








