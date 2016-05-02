import gsmonoms

def fix(relation):
    for monom in relation:
        gsmonoms.removeinvolutions(monom)
    if not gsmonoms.gt(relation[0], relation[1]):
        relation = relation[1], relation[0]
    return relation
    
def compare(lhs, rhs):
    return gsmonoms.compare(lhs[0], rhs[0])
    
def key(relation):
    return gsmonoms.key(relation[0])
    
def make_compositions(lhs, rhs):
    results = []
    szl = len(lhs)
    szr = len(rhs)
    i = 1 - szr
    while i < szl:
        l = lhs[max(0, i):min(i+szr, szl)]
        r = rhs[max(0, -i):min(szr, szl - i)]
        if (l == r):
            print l, r
        i += 1
