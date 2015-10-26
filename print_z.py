def print_z(num):
	"""
	>>> print_z(5)
	1 2 3 4 5
	      6
	    7
	  8
	9 0 1 2 3
	>>> print_z(3)
	1 2 3
	  4
	5 6 7
	>>> print_z(2)
	1 2
	3 4
	"""
    num = 1
    for i in xrange(n):
    	for j in xrange(n):
    		if i == 0 or i == n-1:
    			print num % 10,
	        	num += 1
	        elif j == (n - (i+1)):
	        	print num % 10,
	    		num += 1
      		else:
	        	print ' ',
	    	print 

if __name__ == "__main__":
    from doctest import testmod
    print
    if testmod().failed == 0:
        print "    ** ALL TESTS PASS. GOOD WORK! **"
    print
