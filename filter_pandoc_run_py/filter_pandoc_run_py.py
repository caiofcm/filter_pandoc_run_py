#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "python" into python output
"""

import os
import sys
import json

from pandocfilters import toJSONFilter, Para, Image, \
	get_filename4code, get_caption, get_extension, \
	get_value, Emph, Str, CodeBlock
# from RestrictedPython import compile_restricted
# from RestrictedPython.compile import compile_restricted_exec
# from RestrictedPython import safe_builtins
# from RestrictedPython.PrintCollector import PrintCollector
from .PrintCollector import PrintCollector

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
code_locals = {'_print_': PrintCollector}  # , '_getattr_': None

############################################
###########################################
#
#
# 	 Start Functions Definitions 	 
#
#
###########################################
###########################################

def gambiarra_debugger(*arg, append=True):
	mode = 'a' if append else 'w'
	with open("debugger.txt", mode) as myfile:
		for a in arg:
			myfile.write(a + '\n')


def read_json(filename):
	with open(os.path.join(dir_path, filename), 'r') as fp:
		dt = json.load(fp)
	return dt

# def run_code_restricted(source_code):
# 	try:
# 			byte_code, errors = compile_restricted_exec(source_code)[0:2]
# 			exec(byte_code, {'__builtins__': safe_builtins}, code_locals)
# 	except SyntaxError as e:
# 			raise e
# 			return '<font color="red">Code failed to Run</font>'
# 	pass

def run_code(source_code):
	try:
			# byte_code, errors = compile(source_code, '<inline>')[0:2]
			exec(source_code, {}, code_locals)  # {'__builtins__': safe_builtins}
	except SyntaxError as e:
			raise e
			return '<font color="red">Code failed to Run</font>'
	pass

def adjust_print_output(printed_var):
	return [Para([Str('Output:')]), Para([Str(printed_var)])]

# def run_py_code_block_restricted(key, value, format, meta):
# 	return_ast = []
# 	if key == 'CodeBlock':
# 		[[ident, classes, keyvals], code] = value
# 		if "python" in classes:
# 			caption, typef, keyvals = get_caption(keyvals)
# 			run_code_restricted(code)
# 			show_inpt = list(filter(lambda v: v[0] == 'show_input', keyvals))
# 			if show_inpt is not None and show_inpt[0][1]:
# 				ast_code = CodeBlock(value[0], value[1])
# 				return_ast.append(ast_code)

# 			if '_print' in code_locals:
# 				ast_print = adjust_print_output(code_locals['_print']())
# 				return_ast += ast_print
			
# 			return return_ast
# 	pass


def run_py_code_block(key, value, format, meta):
	return_ast = []
	if key == 'CodeBlock':
		[[ident, classes, keyvals], code] = value
		if "python" in classes:
			caption, typef, keyvals = get_caption(keyvals)
			run_code(code)
			show_inpt = list(filter(lambda v: v[0] == 'show_input', keyvals))
			if show_inpt is not None and show_inpt[0][1]:
				ast_code = CodeBlock(value[0], value[1])
				return_ast.append(ast_code)

			if '_print' in code_locals:
				ast_print = adjust_print_output(code_locals['_print']())
				return_ast += ast_print

			return return_ast
	pass

def behead(key, value, format, meta):
	if key == 'Header' and value[0] >= 2:
		return Para([Emph(value[2])])

def caps(key, value, format, meta):
	if key == 'Str':
		gambiarra_debugger(value)
		return Str(value.upper())

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
