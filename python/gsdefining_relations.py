import gsmonoms

def fix(relation):
    for monom in relation:
        gsmonoms.removeinvolutions(monom)
    if not gsmonoms.gt(relation[0], relation[1]):
        relation = relation[1], relation[0]
    return relation

def compare(lhs, rhs):
    return gsmonoms.compare(lhs[0], rhs[0]) or \
            gsmonoms.compare(lhs[1], rhs[1])

def key(relation):
    return gsmonoms.key(relation[0]), gsmonoms.key(relation[1])
