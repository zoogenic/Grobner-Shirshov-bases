import sys, getopt
import csv
import ast
import gsmonoms
import gsdefining_relations

def helpmessage():
    print "Usage:\n    start.py -r <defining relations file>"

def main(argv):
    relationsfile = ''
    try:
        opts, args = getopt.getopt(argv, "hr:", ["relations="])
    except getopt.GetoptError:
        helpmessage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            helpmessage()
            sys.exit()
        elif opt in ("-r", "--relations"):
            relationsfile = arg

    if not relationsfile:
        helpmessage()
        sys.exit()

    defining_relations = []

    try:
        with open(relationsfile, 'r') as f:
            for line in f:
                rel = ast.literal_eval(line)
                fixed_rel = gsdefining_relations.fix(rel)
                defining_relations.append(fixed_rel)

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit()
    except TypeError as e:
        print "Type error: {0}".format(e)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        sys.exit()

    print '\n'.join(map(str, defining_relations))

    # print "===================="
    # cmp_list = defining_relations[:]
    # cmp_list.sort(cmp = gsdefining_relations.compare)
    # print '\n'.join(map(str, cmp_list))
    print "===================="
    key_list = defining_relations[:]
    key_list.sort(key = gsdefining_relations.key)
    print '\n'.join(map(str, key_list))


if __name__ == "__main__":
    main(sys.argv[1:])
