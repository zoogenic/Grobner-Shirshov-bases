import sys, getopt
import csv
import ast
import gsmonoms
import gsdefining_relations

def helpmessage():
    print "Usage:\n    start.py -m <monomFile>"

def main(argv):
    monomfile = ''
    try:
        opts, args = getopt.getopt(argv, "hm:", ["monoms="])
    except getopt.GetoptError:
        helpmessage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            helpmessage()
            sys.exit()
        elif opt in ("-m", "--monoms"):
            monomfile = arg

    defining_relations = []

    try:
        with open(monomfile, 'r') as f:
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

    print "===================="
    defining_relations.sort(key = gsdefining_relations.key)
    print '\n'.join(map(str, defining_relations))


if __name__ == "__main__":
    main(sys.argv[1:])