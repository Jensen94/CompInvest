title = "The First Test"
directions = "sit back and relax a while"

"""attempting to run simple functions in command prompt"""
def multiplier(x,y):
	answer = int(x)*int(y)
	return answer
	
def prompt_printer():
	print (title)
	print (directions)
	x = input('Please input one number to be muliplited: ')
	y = input('Please eneter a second number: ')
	answer = multiplier(x,y)
	print ("Your input " + str(x) + " and " + str(y) + " is equal to " + str(answer))
	
prompt_printer()	