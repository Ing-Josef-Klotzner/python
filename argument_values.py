# Measure some strings:
# -*- coding: iso-8859-15 -*-
def ask_ok(prompt, retries=4, complaint='Yes or no, ja oder nein please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y','ye','yes','ja'): 
			print "\nguter Mann"
			return True
		if ok in ('n','no','na','nop','nope','nein'): 
			print "\nna dann lern mal brav weiter"
			return False
		retries = retries - 1
		if retries < 0: raise IOError, 'refusenik user'
		print complaint
ask_ok('Verstehst Du Python wirklich?')
