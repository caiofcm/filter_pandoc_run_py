from RestrictedPython import compile_restricted
from RestrictedPython import safe_builtins
from RestrictedPython.PrintCollector import PrintCollector
# import RestrictedPython.SelectCompiler.RCompile.compile_restricted as compile_restricted

# import RestrictedPython.RCompile


def safe_mode():

	source_code = """
def example():
	return 'Hello World!'
"""
	loc = {}
	# byte_code = compile_restricted(source_code, '<inline>', 'exec')
	# exec(byte_code, safe_builtins, loc)
	try:
			byte_code = compile_restricted(source_code,
																		filename='<inline code>',
																		mode='exec')

			exec(byte_code, {'__builtins__': safe_builtins}, loc)
	except SyntaxError as e:
			raise e
	a = loc['example']()
	print(a)


def unsafe_mode():

	source_code = """
import os
a = os.listdir('/')
os.system('del .\tests\crap.txt')
# print('Hello!')
"""
	# loc = {}
	byte_code = compile_restricted(source_code, '<inline>', 'exec')
	exec(byte_code,  {'__builtins__': safe_builtins}, {})
	# a = loc['example']()
	# print(a)


if __name__ == '__main__':
	safe_mode()

	unsafe_mode()
