
# Executing python codes in a markdown file


## Regular block code

A regular markdown code definition

Syntax: \{.python}

```{.python }
e = 'foo'
```

## A runnable block code

For a runnable code append the class .run

Syntax: \{.python .run}

```{.python .run}
d = 1e3
```

## A runnable inline code

An inline code can also be run in python.

Syntax: \`(code)\`\{.run\}

Water density is `foo = 1`{.run}.

## A runnable code with print statement

### Printing to a BlockQuote

Run a python code and show the print output. 

Syntax: \{.python .run format=[blockquote (default), text]\}

```{.python .run}
m = 2 * d
print('The total mass is {:.2f} $m^3$'.format(m))
```

### Printing to regular Paragraph

```{.python .run format=text}
m = 2 * d
print('The total mass is {:.2f} $m^3$'.format(m))
```

## A runnable code with print statement hiding the code block

Run a python code and show the print output, but hiding the code.

Syntax is \{.python .run format=[blockquote (default), text]\ hide_code=[False, True]}

```{.python .run hide_code=True}
m = 2 * d
print('Variable d is {}'.format(d))
```

## A runnable inline code with print statement

It will replace the inline code by the print function output

Syntax: \`(print(code))\`\{.run\}

Obs: It is returned the raw string (math mode will not work)

Water density is `print(d)`{.run} $kg/m^3$ and the total mass was `print('{:.2f} $m^3$'.format(m))`{.run}
