import sys, getopt
import csv
import monoms.removeinvolutions

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
			
	monoms = []
			
	try:
		with open(monomfile, 'r') as f:
			monoms = list(csv.reader(f))
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit()
	except TypeError as e:
		print "Type error({0}): {1}".format(e.errno, e.strerror)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit()
			
	#print 'Monom file is:', monomfile
	print monoms
	

	
		
if __name__ == "__main__":
	main(sys.argv[1:])