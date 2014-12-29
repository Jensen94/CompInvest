title = "The First Test"
directions = "sit back and relax a while"

"""attempting to run simple functions in command prompt"""
def multiplier(x,y,z):
	answer = int(x)*int(y)*int(z)
	return answer
	
def prompt_printer():
	print (title)
	print (directions)
	x = input('Please input one number to be muliplited: ')
	y = input('Please eneter a second number: ')
	z = input('Please enter a third number: ')
	answer = multiplier(x,y,z)
	print ("Your input " + str(x) + " and " + str(y) + " and " + str(z) + " is equal to " + str(answer))
	
prompt_printer()	