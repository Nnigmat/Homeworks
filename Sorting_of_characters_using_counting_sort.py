'''
 Task: Write a program that takes as input N characters (each of which can be one of English lower case letter), and sort them in lexicographic order. For example, if the input is

z c a a

then the output should be

a a c z

Implement your program by using the counting sort.
'''

def sort(arr):
    count = [0] * 26
    delta = 97

    for ltr in arr:
        count[ord(ltr) - delta] += 1

    result = ''
    for i in range(0, 26):
        if count[i] != 0:
            result += (chr(i + delta) + ' ') * count[i]

    return result


inp = open('input.txt', 'r')
out = open('output.txt', 'w')
out.write(sort(list(inp.readline().split(' '))))
inp.close()
