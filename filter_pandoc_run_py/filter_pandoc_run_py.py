#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "python" into python output
"""

import os
import sys
from shutil import which
from subprocess import Popen, PIPE
import json
import re
try:
		from StringIO import StringIO
except ImportError:
		from io import StringIO
import contextlib

from pandocfilters import *

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
code_locals = {'fig_counter': 0, 'used_fig_num': []}


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


def from_txt_to_ast_pandoc_code(printed_var):
	# if breakLine:
	# 	printed_var = "\n\n".join(printed_var.split("\n"))
	txt_as_pandoc_obj_str = run_pandoc(printed_var)
	out = "\n".join(txt_as_pandoc_obj_str.splitlines())  # Replace \r\n with \n
	txt_as_pandoc_obj = json.loads(txt_as_pandoc_obj_str)
	metaData = txt_as_pandoc_obj['meta']
	astCode = txt_as_pandoc_obj['blocks']
	return metaData, astCode

def adjust_print_output(printed_var, format_type = None):
	format_type = 'blockquote' if format_type is None else format_type
	if format_type == 'blockquote':
		printed_var = "\n\n".join(printed_var.split("\n"))
		txt_as_pandoc_obj = from_txt_to_ast_pandoc_code(printed_var)
		cod = [	BlockQuote([Para([Str('Output:')]), 
						BlockQuote(txt_as_pandoc_obj[1])])]
	elif format_type == 'text':
		txt_as_pandoc_obj = from_txt_to_ast_pandoc_code(printed_var)
		cod = txt_as_pandoc_obj[1]
	return cod

def get_key_in_keyval_list(keyvals, key, fallback_not_found):
	value = fallback_not_found
	for kw in keyvals:
		if key == kw[0]:
			value = kw[1]
			break
	return value

def handle_inline_plot(code, classes, keyvals, format, ident):
	plt = code_locals['plt']
	fignums = plt.get_fignums()
	kw = keyvals
	ast_ret_code = []
	md_code = ''
	last_number_counter = len(code_locals['used_fig_num'])
	# ast_fig_kw = kw.copy() #addition keyvalus ? todo
	for num in fignums: #and num not in code_locals['used_fig_num']:
		if num in code_locals['used_fig_num']:
			continue
		unique_code = repr(plt.figure(num)) + str(num)
		fname = get_filename4code("plt", unique_code)
		num_mod = num - last_number_counter

		use_title = bool(get_key_in_keyval_list(kw, 'title_as_caption', False))
		if not use_title:
			kw_cap = 'caption{}'.format(num_mod) if num_mod > 1 else 'caption'
			caption = get_key_in_keyval_list(kw, kw_cap, '')  # fname.split('\\')[1]
		else:
			caption = plt.gca().title._text

		# kw_lbl = 'label{}'.format(num_mod) if num_mod > 1 else 'label'
		# label = get_key_in_keyval_list(kw, kw_lbl, 'label-{}'.format(num))
		
		# kw_wdth = 'width{}'.format(num) if num > 1 else 'width'
		# width = get_key_in_keyval_list(kw, kw_wdth, '')

		# Parei aqui-> figures attribute
		kw_figattr = 'figattr{}'.format(num_mod) if num_mod > 1 else 'figattr'
		figattr_raw = get_key_in_keyval_list(kw, kw_figattr, '')
		if figattr_raw != '':
			figattr_id, figattr_kws = figattr_str_convertion(figattr_raw)
		else:
			figattr_id, figattr_kws = '', [] 

		kw_ext = 'ext{}'.format(num) if num > 1 else 'ext'
		ext = get_key_in_keyval_list(kw, kw_ext, 'png')
		
		filePath = '{}.{}'.format(fname, ext)
		plt.savefig(filePath, format=ext)
		ast_ret_code += [Para([Image([figattr_id, [], figattr_kws],
                               [Str(caption)], [filePath, "fig:"])])]	
		code_locals['used_fig_num'].append(num)
	return ast_ret_code

def figattr_str_convertion(s):
	fig_id = re.findall(r'#([\w\:]+)', s)
	if len(fig_id)  == 0:
		raise ValueError('Error capturing figure ID.')
	elif len(fig_id) > 1:
		raise ValueError('Error capturing figure ID. Use single figure ID')
	kws = re.findall(r'(\w+)=([\w\'\.\:]+)', s)
	return fig_id[0], kws


def workaround_classes_with_commonmark_syntax(code, classes, keyvals, value):
	'''
	Configuration string as a pytho comment to get classes and key-vals
	Example of configuration: #filter: {.c1 .c2 key1=val1 key2="value 2" }
	'''
	try:
		re.search(r'^\s*#\s*filter:\s+{', code).group()
	except AttributeError:
		return
	filter_configs = code[code.find("{") + 1:code.find("}")]
	found_class = re.findall(r'\.(\w+)', filter_configs)
	kw_pairs_simple = re.findall(r'(\w+)=(\w+)', filter_configs)
	# kw_pairs_cplx = re.findall(r'(\w+)=("[\w\-\s]+")', filter_configs)
	kw_pairs_cplx = re.findall(r'(\w+)=("[^"]+")', filter_configs)	
	found_keyvals = kw_pairs_simple + kw_pairs_cplx
	classes += found_class
	keyvals += found_keyvals
	# Modiy Value to remove filter line:
	value[1] = code[code.find("}")+1:]
	return

def run_py_code_block(key, value, format, meta):
	return_ast = []
	if key == 'CodeBlock':
		[[ident, classes, keyvals], code] = value
		workaround_classes_with_commonmark_syntax(code, classes, keyvals, value)

		if "python" in classes and "run" in classes:
			# caption, typef, keyvals = get_caption(keyvals)
			
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

			if 'plt' in code_locals:
				fignums = code_locals['plt'].get_fignums()
				if len(fignums) > 0:
					ast_figure = handle_inline_plot(code, classes, keyvals, format, ident)
					# code_locals['plt'].close('all')
					return_ast += ast_figure
				# Continue from here:
				# https://github.com/jgm/pandocfilters/blob/master/examples/plantuml.py

			return return_ast
	elif key == 'Code':
		[[ident, classes, keyvals], code] = value
		if "run" in classes:
			printed_string = run_code(code)
			removed_last_line_break = printed_string[0:-1]

			if printed_string:
				metaAst, ast_print = from_txt_to_ast_pandoc_code(removed_last_line_break)
		# 	# ast_print[0]['t'] = 'Str'
		# 		# return_ast.append(ast_print)
				# return_ast.append([Para('Hello you')])
				return ast_print[0]['c']
				# return Str(removed_last_line_break)
				# return RawInline('html', 'Hello')
				# return return_ast
		# 		# return_ast += [Str(removed_last_line_break)]
		# 	# if printed_string:
		# 		return return_ast
		# return Str('Yes!')
	pass

def main():
	toJSONFilter(run_py_code_block)

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
	main()
