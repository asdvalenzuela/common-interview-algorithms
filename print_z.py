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
	# print first line
	num_to_print = 1
	while num_to_print < num:
		print str(num_to_print % 10) + '',
		num_to_print += 1
	print str(num_to_print % 10) + ''
	num_to_print += 1

	# print diagonal
	diagonal = num - 2
	if diagonal != 0:
		space = (num-1) + (num-3)		
		nums_printed = 0
		while nums_printed < diagonal:
			print ' ' * space + str(num_to_print % 10)
			space -= 2
			nums_printed += 1
			num_to_print += 1
	
	# print second line
	line = num
	nums_printed = 0
	while nums_printed < line:
		print str(num_to_print % 10) + '',
		nums_printed += 1
		num_to_print += 1

if __name__ == "__main__":
    from doctest import testmod
    print
    if testmod().failed == 0:
        print "    ** ALL TESTS PASS. GOOD WORK! **"
    print
