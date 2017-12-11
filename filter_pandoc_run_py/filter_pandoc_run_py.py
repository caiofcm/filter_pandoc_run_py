#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "python" into python output
"""

import os
import sys
import json

from pandocfilters import toJSONFilter, Para, Image, get_filename4code, get_caption, get_extension, get_value, Emph, Str
from RestrictedPython import compile_restricted
from RestrictedPython.compile import compile_restricted_exec
from RestrictedPython import safe_builtins
from RestrictedPython.PrintCollector import PrintCollector

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

def gambiarra_debugger(*arg, append=True):
	mode = 'a' if append else 'w'
	with open("debugger.txt", mode) as myfile:
		for a in arg:
			myfile.write(a + '\n')


def read_json(filename):
	with open(os.path.join(dir_path, filename), 'r') as fp:
		dt = json.load(fp)
	return dt

def run_code_restricted(source_code):
	try:
			byte_code = compile_restricted(source_code,
																	filename='<inline>',
																	mode='exec')

			exec(byte_code, {'__builtins__': safe_builtins}, code_locals)
	except SyntaxError as e:
			raise e
			return '<font color="red">Code failed to Run</font>'
	pass

def run_py_code_block(key, value, format, meta):
	if key == 'CodeBlock':
		[[ident, classes, keyvals], code] = value
		if "python" in classes:
			caption, typef, keyvals = get_caption(keyvals)
			# xx = eval(code)
			# xx = eval("import os;...", {'os': None})
			xx = run_code_restricted(code)
			return [Para([Str('Output:')]), Para([Str(xx)])]

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
