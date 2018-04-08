'''
  
  Task: Grossmeister set the pin code to his mobile phone. He wants to check how secure it is. So he told his friend Hacker that his pin code contains N digits and every two neighbor digits connected with knight move on the telephone keypad. For example button 1 connected with 6 and 8. Grossmeister asks his friend, how many pin codes follows that property?
  
  This program solve it using dynamic programming

'''
def pin(n):
    current_number_of_variants = [1 for _ in range(10)]
    if n == 1:
        return 10
    previous_number_of_variants = None
    adjustment = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [9, 3, 0], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3],
                  9: [2, 4]}
    for _ in range(n - 1):
        previous_number_of_variants = current_number_of_variants.copy()
        for i in range(10):
            if i != 5:
                current_number_of_variants[i] = sum([previous_number_of_variants[j] for j in adjustment[i]])

    return sum(current_number_of_variants) - 1

inp = open('input.txt', 'r')
out = open('output.txt', 'w')
out.write(str(pin(int(inp.read()))))
inp.close()
