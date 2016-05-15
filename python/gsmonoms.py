def removeinvolutions(numbers):
    i = 0 
    prev = None
    while i < len(numbers):
        number = numbers[i]
        if number == prev:
            numbers.pop(i) # Current
            numbers.pop(i - 1) # Previous
            i -= 1 # We deleted two, so the next is back one
        else:
            i += 1
        if i:
            prev = numbers[i - 1]
        else:
            prev = None
    return numbers

def gt(lhs, rhs):
    lenl = len(lhs)
    lenr = len(rhs)
    if lenl == lenr:
        return rhs > lhs
    return lenl > lenr

def compare(lhs, rhs):
    # return (len(lhs) - len(rhs)) or cmp(rhs, lhs)
    return (len(rhs) - len(lhs)) or cmp(lhs, rhs)

def key(lst): #induce reverse order
    return -len(lst), lst
