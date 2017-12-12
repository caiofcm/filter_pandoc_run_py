# pandoc-run-python


*pandoc-run-python* is a [pandoc] filter for execute python codes written in `CodeBlocks` or inline `Code`. It receives the print statement output and place it to the markdown converted file. OBS: Code has to be **trusted**

[pandoc]: http://pandoc.org/

<!-- https://github.com/chdemko/pandoc-latex-fontsize as reference -->

## Documentation

See the [wiki pages](https://github.com/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    pandoc INFILE -F filter_pandoc_run_py --to FORMAT -o OUTFILE

Tested only from markdown to markdown / html

## Installation

*pandoc-run-python* requires [python] (tested in version > 3.0)

Install *pandoc-run-python* as root using the bash command

    git clone URL
		cd dir
		pip install .


## How to Use It

Create a regular markdown code but appending a class .run to it.

### For `CodeBlock`

The syntax is: Syntax: \{.python .run format=[blockquote (default), text] hide_code=[False (default), True] \}

"Pretty print" enable: output of print statement is converted and is rendered

### For `Code`

The syntax is \`(print(code))\`\{.run\}

"Pretty print" unable: output is the raw print statement output string

## Example

From a markdown file such as:

```{.python .run}
d = 1e3
m = 2 * d
print('The total mass is {:.2f} $m^3$'.format(m))
```

`pandoc FILE --to markdown -F filter_pandoc_run_py.py -o OUTFILE.md`

```{.markdown}
> Output:
>
> > The total mass is 2000.00 $m^3$
```

## Getting Help

If you have any difficulties with *pandoc-run-python*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/




