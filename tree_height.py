# Patriks Jasinovičs 221RDB082 13.grupa
# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    path_lengths = numpy.zeros(n)
    for x in range(n):
        length = 0
        if parents[x] == -1:
            path_lengths[x] = 0
        else:
            temp = x
            while parents[temp] != -1:
                temp = parents[temp]
                length += 1
            path_lengths[x] = length + 1

            
    return max(path_lengths)


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
