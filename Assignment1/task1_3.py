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
    middle = int(len(x) / 2)

    # Firstly multiply two left parts of arrays
    res = multiply(x[0:middle], y[0:middle])

    # Store to str_ll result of multiplication
    # for using int(str, 2) to transpose binary number to decimal
    str_ll = ''
    for el in res:
        str_ll += str(el)

    # Secondly multiply right parts of arrays
    res = multiply(y[middle: len(y)], x[middle: len(x)])

    # Store to str_rr result of multiplication
    # for using int(str, 2) to transpose binary number to decimal
    str_rr = ''
    for el in res:
        str_rr += str(el)

    # We store left and right parts of each arrays to string
    # for adding them using int(str, 2)
    str_yl = ''
    for i in range(0, middle):
        str_yl += str(y[i])
    str_xl = ''
    for i in range(0, middle):
        str_xl += str(x[i])
    str_yr = ''
    for i in range(middle, len(y)):
        str_yr += str(y[i])
    str_xr = ''
    for i in range(middle, len(x)):
        str_xr += str(x[i])

    # Add left parts to rights
    x_es = bin(int(str_xl, 2) + int(str_xr, 2))
    y_es = bin(int(str_yl, 2) + int(str_yr, 2))

    # Make list from binary numbers which looks like '0b...'
    # After multiply two numbers
    res = multiply(list(map(int, list(x_es.split('b')[1]))), list(map(int, list(y_es.split('b')[1]))))

    # Again given result translate to string type
    str_end = ''
    for el in res:
        str_end += str(el)

    # Calculate all elements by using formula
    res = bin(int(str_ll, 2) * (2 ** (middle * 2)) + (int(str_end, 2) - int(str_rr, 2) - int(str_ll, 2))
              * (2 ** middle) + int(str_rr, 2))

    # Split given number and return array of integers of its numbers
    res = list(map(int, list(res.split('b')[1])))
    return res


# Variables for reading and writing
inp = open("input.txt", 'r')
out = open("output.txt", 'w')

result = multiply(list(map(int, list(inp.readline().strip()))), list(map(int, list(inp.readline().strip()))))

for el in result:
    out.write(str(el))

inp.close()
out.close()
