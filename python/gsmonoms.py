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
    return (len(rhs) - len(lhs)) or cmp(lhs, rhs)

def key(lst): #induce reverse order
    return -len(lst), lst

def get_intersect_additions(lhs, rhs):
    szl = len(lhs)
    szr = len(rhs)
    for i in xrange(1 - szr, szl):
        lhsl = max(0,  i)
        rhsl = max(0, -i)
        lhsr = min(szr + i, szl)
        rhsr = min(szr, szl - i)
        
        if lhs[lhsl:lhsr] == rhs[rhsl:rhsr]:
            u = rhs[:rhsl]
            v = rhs[rhsr:]
            w = lhs[:lhsl]
            t = lhs[lhsr:]
            assert u + lhs + v == w + rhs + t
            yield u, v, w, t
            

if __name__ == "__main__":
    a = [1,2,5,7,6,9,1,3,1,2,6,6,3,1,2,6,1,3]
    b = [3,1,2]
    for u, v, w, t in get_intersect_additions(a, b):
        print "u = %s, v = %s\nw = %s, t = %s\n" % (u, v, w, t)
    print "==========================="
    for u, v, w, t in get_intersect_additions(b, a):
        print "u = %s, v = %s\nw = %s, t = %s\n" % (u, v, w, t)
