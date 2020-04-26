'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

'''

def hello_name(name):

	#This problem uses the idea of concatination. 
	#Watch: People often miss the space 
	return "Hello " + name + "!"