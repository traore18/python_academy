# define the methode that takes a list of integers
def challenge(number_list):
	i = 0
	while i < len(number_list):
		if number_list[i] % 2 == 0:
			
			print "Index at: %d" % i
			print number_list[i]
		else:
			print number_list[i]
			print "Odd"
		
		i = i + 1
my_list = [45, 2, 89, 77, 66, 100, 1234192342, 234, 10]

challenge(my_list)