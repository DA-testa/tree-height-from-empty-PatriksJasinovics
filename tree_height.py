# Patriks Jasinovičs 221RDB082 13.grupa
# Visi testi izpildās, bet viens tests iet ilgāk par 4 minūtēm, tāpēc ir runtime error,
# Es domāju, ka tas notiek tagad, jo autograding tiek izpildīts tieši pirms termiņa beigām,
# kad visa fakultāte noslogo šo codespace tādejādi neizpildot šo testu 4 minūšu laikā

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
            
    return int(max(path_lengths))


def main():
    input_method = input()
    # implement input from keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    if 'I' in input_method:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    
    if 'F' in input_method:
        file_name = input()
        path = 'test/' + file_name

        if 'a' not in file_name:
            try:
                with open(path, 'r') as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    print(compute_height(n, parents))
            except Exception as e:
                print('An Error occured:', str(e))
                return
        else:
            print('Incorrect file name')    
            return       



    
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
