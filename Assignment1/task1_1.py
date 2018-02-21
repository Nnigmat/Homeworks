def multiply(x, y):
    # If we get one of arrays with length equal 1 then
    # return y if x==1 else return 0
    if len(x) == 1:
        if x[0] == 1:
            return y
        else:
            return [0]

    # The same when we have y equal to 1
    elif len(y) == 1:
        if y[0] == 1:
            return x
        else:
            return [0]

    # Make equal sized arrays x and y, also they need to be power of 2
    if len(x) < len(y):

        # If length of y is odd(вродь нечетная) then we insert 0 to start of array
        # to make length even
        if len(y) % 2 != 0:
            y.insert(0, 0)

        # Insert zeroes till the length of arrays will be equal
        i = len(x)
        while i < len(y):
            x.insert(0, 0)
            i += 1
    else:

        # If length of x is odd(вродь нечетная) then we insert 0 to start of array
        # to make length even
        if len(x) % 2 != 0:
            x.insert(0, 0)

        # Insert zeroes till the length of arrays will be equal
        i = len(y)
        while i < len(x):
            y.insert(0, 0)
            i += 1

    # Make variable middle to store the middle position of array
    middle = int(len(x)/2)

    # Firstly multiply two left parts of arrays and add to the end of array n zeros
    res = multiply(x[0:middle], y[0:middle]) + [0] * middle * 2

    # Transpose res to string for using int(str, 2) which transpose given binary number to decimal
    str_res_first = ''
    for el in res:
        str_res_first += str(el)

    # Secondly multiply left part of first array and right part of second
    res = multiply(x[0:middle], y[middle:len(y)])

    # Transpose res to string for using int(str, 2) which transpose given binary number to decimal
    str_res_second = ''
    for el in res:
        str_res_second += str(el)

    # Thirdly multiply right part of first array and left part of second
    res = multiply(y[0:middle], x[middle: len(x)])

    # Transpose res to string for using int(str, 2) which transpose given binary number to decimal
    str_res_third = ''
    for el in res:
        str_res_third += str(el)

    # Lastly multiply right parts of arrays
    res = multiply(y[middle: len(y)], x[middle: len(x)])

    # Transpose res to string for using int(str, 2) which transpose given binary number to decimal
    str_res_fourth = ''
    for el in res:
        str_res_fourth += str(el)

    # Calculate all elements by using formula
    res = bin(int(str_res_first, 2) + (int(str_res_second, 2) + int(str_res_third, 2))*(2**middle)\
          + int(str_res_fourth, 2))

    # Split given number and return array of integers of its numbers
    res = list(map(int,list(res.split('b')[1])))
    return res


# Variables for reading and writing
inp = open("input.txt", 'r')
out = open("output.txt", 'w')

result = multiply(list(map(int, list(inp.readline().strip()))), list(map(int, list(inp.readline().strip()))))

for el in result:
    out.write(str(el))

inp.close()
out.close()