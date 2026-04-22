more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. 1,2,3,4
print()                               # What is the value of more at this point? [2,3,4,5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. 1, returns 1; 2, returns 4; 3, returns 9; 4, returns 16.


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? squares is [1,4,9,16], this is a list of all returned values from square().

# def check(n:int) -> bool:
#    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0, returns False; 1, returns False; 2, returns False; 3, returns True; 4, returns True


answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print()

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. 3, returns 4; 4, returns 5


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 0, returns False; 1, returns False; 2, returns False; 3, returns True; 4, returns True


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5]
print()