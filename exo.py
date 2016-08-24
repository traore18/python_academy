def print_list(number_list):
    for i in number_list:
	    if i > 20:
		    print "Big Number"
	    else:
		    print "Small Number"
my_list = [1, 3, 10, 24, 400, 4, 100000]


print_list(my_list)

def keep_printing(number_list):
	i = 0
	while i < len(number_list):
		print "Index at %d" % i
		print number_list[i]
		i = i + 1
		
keep_printing(my_list)