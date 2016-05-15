def gstest(lhs, rhs):
    results = []
    szl = len(lhs)
    szr = len(rhs)
    i = 1 - szr
    while i < szl:
        l = lhs[max(0, i):min(i+szr, szl)]
        r = rhs[max(0, -i):min(szr, szl - i)]
        if (l == r):
            # print l, r
           print rhs[0:max(0, -i)], lhs, rhs[min(szr, szl - i):szr]
           print lhs[0:max(0,i)], rhs, lhs[min(i + szr,szl):szl]
           print
        i += 1

def gstest1(lhs, rhs):
    results = []
    szl = len(lhs)
    szr = len(rhs)
    i = 1 - szr
    while i < szl:
        a = max(0, i)
        b = max(0, -i)
        c = min(i+szr, szl)
        d = min(szr, szl - i)

        if (lhs[a:c] == rhs[b:d]):
            u = rhs[0:b]
            v = rhs[d:szr]
            w = lhs[0:a]
            t = lhs[c:szl]
            results.append((u, v, w, t))
        i += 1
    return results
