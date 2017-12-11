import os
import sys
import json
from filter_pandoc_run_py import *

import RestrictedPython

compiler = RestrictedPython.compile.compile_restricted_exec

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_gambiarra_debugger():
	gambiarra_debugger('eu', 'voce', 'tu', 'vos')
	pass

def test_json_ast_reader():
	'''
	Json generated as: pandoc test.md -t json -o test.json
	'''
	dt = read_json(os.path.join(dir_path, 'test.json'))
	assert isinstance(dt, (dict, list))


def test_run_pandoc_like():
	dt = read_json(os.path.join(dir_path, 'test.json'))
	for d in dt[1]:
		run_py_code_block(d['t'], d['c'], 'markdown', None)


def test_os_command():
	cmd = 'ls -al'
	os.system(cmd)


ALLOWED_PRINT_FUNCTION = """
from __future__ import print_function
print ('Hello World!')
"""

def test_print_function__simple_prints():
	loc = {'_print_': PrintCollector, '_getattr_': None}
	code, errors = compiler(ALLOWED_PRINT_FUNCTION)[:2]
	assert errors == ()
	assert code is not None
	exec(code, {}, loc)
	aaa = loc['_print']()
	print(aaa)
	assert loc['_print']() == 'Hello World!\n'


############################################
###########################################
#
#
# 	 Regular Debugger Start
#
#
###########################################
###########################################
def insider_Debugger():
	# generate_json_ast()
	test_run_pandoc_like()
	pass

if __name__ == '__main__':
	insider_Debugger()
