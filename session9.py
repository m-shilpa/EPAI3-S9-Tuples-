from functools import wraps
from datetime import datetime,timezone
from time import perf_counter

# Decorator that allows to run a function only at odd seconds, else prints out "We're even!"
def odd_it(fn: "Function"):
	''' Function that allows a function to run at odd seconds'''
	@wraps(fn)
	def inner(*args, **kwargs):
		''' Decorator that allows a function to run at odd seconds else prints 'We're even '''
		sec = datetime.now().second
		if sec %2 == 0:
			print("We're even!")
		else:
	      		return fn(*args,**kwargs)
	return inner

# The same logger that we coded in the class
# it will be tested against a function that will be sent 2 parameters, and 
# it would return some random string. 
def logger(fn: "Function"):
	
	''' A logger function that gives the details of the function and it's logs'''

	@wraps(fn)
	def inner(*args, **kwargs):
		''' Decorator that gives details such as the function description, it's arguments, when the function was called and it's execution time '''

		exec_start = datetime.now(timezone.utc)
		result = fn(*args,**kwargs)
		exec_end = datetime.now(timezone.utc)
		print(f'Function: {fn.__name__} ')
		print("Function description")
		print(f"This is a function's writeup : {fn.__doc__}")
		print(f'Function annotation : {fn.__annotations__}')
		print(f'{fn.__name__} called at {exec_start}')       
		print(f'Execution time of {fn.__name__} : {exec_end - exec_start}')

		return result
	return inner



# start with a decorator_factory that takes an argument one of these strings, 
# high, mid, low or no
# then write the decorator that has 4 free variables
# based on the argument set by the factory call, give access to 4, 3, 2 or 1 arguments
# to the function being decorated from var1, var2, var3, var4
# YOU CAN ONLY REPLACE "#potentially missing code" LINES WITH MULTIPLE LINES BELOW
# KEEP THE REST OF THE CODE SAME
def decorator_factory(access:str):
	pass


# The authenticate function. Start with a dec_factory that sets the password. It's inner
# will not be called with "password", *args, **kwargs on the fn
def authenticate(set_password):
	pass


# The timing function
def timed(reps):
    pass
