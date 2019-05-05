# filter_pandoc_run_py 

[![Build Status](https://img.shields.io/travis/caiofcm/filter_pandoc_run_py/master.svg)](https://travis-ci.org/caiofcm/filter_pandoc_run_py/branches)
[![Coverage Status](https://coveralls.io/repos/github/caiofcm/filter_pandoc_run_py/badge.svg?branch=master)](https://coveralls.io/github/caiofcm/filter_pandoc_run_py?branch=master)
[![PyPI version](https://img.shields.io/pypi/v/filter_pandoc_run_py.svg)](https://pypi.org/project/filter_pandoc_run_py/)
[![PyPI format](https://img.shields.io/pypi/format/filter_pandoc_run_py.svg)](https://pypi.org/project/filter_pandoc_run_py/)
[![License](https://img.shields.io/pypi/l/filter_pandoc_run_py.svg)](https://raw.githubusercontent.com/caiofcm/filter_pandoc_run_py/master/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/filter_pandoc_run_py.svg)](https://pypi.org/project/filter_pandoc_run_py/)
[![Development Status](https://img.shields.io/pypi/status/filter_pandoc_run_py.svg)](https://pypi.org/project/filter_pandoc_run_py/)

*filter_pandoc_run_py* is a [pandoc] filter for execute python codes written in `CodeBlocks` or inline `Code`. It receives the print statement output and place it to the markdown converted file. Also, it save any created pyplot figure to a folder and include it as an image. Code has to be **trusted**

[pandoc]: http://pandoc.org/

<!-- https://github.com/chdemko/pandoc-latex-fontsize as reference -->

## Usage

To apply the filter, use the following option with pandoc:

	pandoc INPUT_FILE -F filter_pandoc_run_py --to OUTPUT_FORMAT -o OUTPUT_FILE

Example:

	pandoc ./tests/test.md -F filter_pandoc_run_py -t gfm -o test_converted.md

- You can convert it to any pandoc supported format;
- When converted to a markdown format it can change some part of the text to conform with the default style (e.g. changing setext-style headers to ATX headers).

## Installation

*filter_pandoc_run_py* requires [python] (tested in version > 3.0)

Install *filter_pandoc_run_py* as root using the bash command

	git clone URL
	cd dir
	pip install .

Or get it from PYPI:

	pip install filter_pandoc_run_py


## How to Use It

Create a regular markdown code but appending a class .run to it.

### For `CodeBlock`

Output print statement as a BlockQuote or paragraph. You can hide the generation code.

Syntax: `{.python .run format=[blockquote (default), text] hide_code=[False (default), True] }`

The following syntax is also support for enabling standard IDE code highlight:

	```python
	#filter: {.run format=[blockquote (default), text] hide_code=[False (default), True] }
	.... code ....
	```

"Pretty print" enable: output of print statement is converted and is rendered

### For `Code`

Output print statement as inline text.

The syntax is:

	`print(code)`{.run}

"Pretty print" enable: output of print statement is converted and is rendered

## Example

From a markdown file such as:

	```{.python .run}
	d = 1e3
	m = 2 * d
	print('The total mass is {:.2f} $m^3$'.format(m))
	```

`pandoc FILE --to markdown -F filter_pandoc_run_py -o OUTFILE.md`

```{.markdown}
> Output:
>
> > The total mass is 2000.00 $m^3$
```

Generating pyplot images embedded in markdown file:

	```{.python .run caption="Figure Number One" label="my_fig"}
	import matplotlib
	matplotlib.use('AGG')
	from matplotlib import pyplot as plt
	plt.plot([1, 2], [3, 4], 'dr-')
	```

### More examples

- Check files `./tests/test.md` and `./tests/test_common_mark.md`

## Getting Help

If you have any difficulties with *filter_pandoc_run_py*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/caiofcm/filter_pandoc_run_py/issues




