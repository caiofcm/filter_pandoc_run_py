#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "python" into python output
"""

import os
import sys
import json
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import contextlib

from pandocfilters import toJSONFilter, Para, Image, \
	get_filename4code, get_caption, get_extension, \
	get_value, Emph, Str, CodeBlock
# from .PrintCollector import PrintCollector

############################################
###########################################
#
#
# 	 Global Scope 	 
#
#
###########################################
###########################################

dir_path = os.path.dirname(os.path.realpath(__file__))
# code_locals = {'_print_': PrintCollector}  # , '_getattr_': None
code_locals = {}

############################################
###########################################
#
#
# 	 Start Functions Definitions 	 
#
#
###########################################
###########################################

def read_json(filename):
	with open(os.path.join(dir_path, filename), 'r') as fp:
		dt = json.load(fp)
	return dt

@contextlib.contextmanager
def stdoutIO(stdout=None):
	'''
	code = """
i = [0,1,2]
for j in i :
    print(j)
"""
	with stdoutIO() as s:
		exec(code)

	print("out:", s.getvalue())
	assert s.getvalue() == '0\n1\n2\n'
	'''	
	old = sys.stdout
	if stdout is None:
		stdout = StringIO()
	sys.stdout = stdout
	yield stdout
	sys.stdout = old

def run_code(source_code):
	try:
			# byte_code, errors = compile(source_code, '<inline>')[0:2]
		# exec(source_code, {}, code_locals)  # {'__builtins__': safe_builtins}
		with stdoutIO() as s:
			exec(source_code, {}, code_locals)
		print_string = s.getvalue()
	except SyntaxError as e:
		raise e
		print_string = '<font color="red">Code failed to Run</font>'
	return print_string

def adjust_print_output(printed_var):
	return [Para([Str('Output:')]), Para([Str(printed_var)])]

def run_py_code_block(key, value, format, meta):
	return_ast = []
	if key == 'CodeBlock':
		[[ident, classes, keyvals], code] = value
		if "python" in classes:
			caption, typef, keyvals = get_caption(keyvals)
			
			printed_string = run_code(code)

			show_inpt = list(filter(lambda v: v[0] == 'show_input', keyvals))
			if show_inpt is not None and show_inpt[0][1] != 'False':
				ast_code = CodeBlock(value[0], value[1])
				return_ast.append(ast_code)

			if printed_string:
				ast_print = adjust_print_output(printed_string)
				return_ast += ast_print

			return return_ast
	pass

############################################
###########################################
#
#
# 	 Start 	 
#
#
###########################################
###########################################

if __name__ == "__main__":
	toJSONFilter(run_py_code_block)
