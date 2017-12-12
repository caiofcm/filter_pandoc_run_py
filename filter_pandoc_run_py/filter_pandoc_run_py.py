#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "python" into python output
"""

import os
import sys
from shutil import which
from subprocess import Popen, PIPE
import json
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import contextlib

# from pandocfilters import toJSONFilter, Para, Image, \
# 	get_filename4code, get_caption, get_extension, \
# 	get_value, Emph, Str, CodeBlock, Code, BlockQuote, \
# 	walk, applyJSONFilters
from pandocfilters import *
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
# 	 Aux Functions 	 
#
#
###########################################
###########################################

def run_pandoc(text='', args=['--from=markdown', '--to=json']):
	"""
	Low level function that calls Pandoc with (optionally)
	some input text and/or arguments
	Reference: http://scorreia.com/software/panflute/_modules/panflute/tools.html#run_pandoc
	"""
	pandoc_path = which('pandoc')
	if pandoc_path is None or not os.path.exists(pandoc_path):
			raise OSError("Path to pandoc executable does not exists")

	proc = Popen([pandoc_path] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate(input=text.encode('utf-8'))
	exitcode = proc.returncode
	if exitcode != 0:
			raise IOError(err)
	return out.decode('utf-8')

############################################
###########################################
#
#
# 	 Start Functions Definitions 	 
#
#
###########################################
###########################################

def read_json(filename, mode = 'json'):
	with open(os.path.join(dir_path, filename), 'r') as fp:
		if mode == 'json':
			dt = json.load(fp)
		elif mode == 'string':
			dt = fp.read()
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

def adjust_print_output(printed_var, format_type = None):
	format_type = 'blockquote' if format_type is None else format_type
	# return [Para([Str('Output:')]), Para([Str(printed_var)])]
	# printed_var = "<br />".join(printed_var.split("\n"))
	printed_var = "\n\n".join(printed_var.split("\n"))
	txt_as_pandoc_obj_str = run_pandoc(printed_var)
	out = "\n".join(txt_as_pandoc_obj_str.splitlines())  # Replace \r\n with \n
	txt_as_pandoc_obj = json.loads(txt_as_pandoc_obj_str)
	cod = txt_as_pandoc_obj[1]
	if format_type == 'blockquote':
		cod = [BlockQuote([Para([Str('Output:')]), BlockQuote(txt_as_pandoc_obj[1])])]
	elif format_type == 'text':
		cod = txt_as_pandoc_obj[1]
	return cod

def run_py_code_block(key, value, format, meta):
	return_ast = []
	if key == 'CodeBlock':
		[[ident, classes, keyvals], code] = value
		if "python" in classes and "run" in classes:
			caption, typef, keyvals = get_caption(keyvals)
			
			printed_string = run_code(code)

			# show_inpt = list(filter(lambda v: v[0] == 'show_input', keyvals))
			# if show_inpt is not None and show_inpt[0][1] != 'False':
			hide_code = get_value(keyvals, 'hide_code')[0]
			if hide_code is None or hide_code == 'False':
				ast_code = CodeBlock(value[0], value[1])
				return_ast.append(ast_code)

			if printed_string:
				format_type = get_value(keyvals, 'format')[0]
				ast_print = adjust_print_output(printed_string, format_type)
				return_ast += ast_print

			return return_ast
	elif key == 'Code':
		[[ident, classes, keyvals], code] = value
		if "run" in classes:
			printed_string = run_code(code)
			removed_last_line_break = printed_string[0:-1]
			if printed_string:
				return_ast += [Str(removed_last_line_break)]
				return return_ast
	pass


# def deemph(key, val, fmt, meta):
#     if key == 'Emph':
#         return walk(val, 1, fmt, meta)

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
