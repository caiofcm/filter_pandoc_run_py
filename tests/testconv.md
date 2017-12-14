Executing python codes in a markdown file
=========================================

Regular block code
------------------

A regular markdown code definition

Syntax: {.python}

``` {.python}
e = 'foo'
```

A runnable block code
---------------------

For a runnable code append the class .run

Syntax: {.python .run}

``` {.python .run}
d = 1e3
```

A runnable inline code
----------------------

An inline code can also be run in python.

Syntax: \`(code)\`{.run}

Water density is `foo = 1`{.run}.

A runnable code with print statement
------------------------------------

### Printing to a BlockQuote

Run a python code and show the print output.

Syntax: {.python .run format=\[blockquote (default), text\]}

``` {.python .run}
m = 2 * d
print('The total mass is {:.2f} $m^3$'.format(m))
```

> Output:
>
> > The total mass is 2000.00 $m^3$

### Printing to regular Paragraph

``` {.python .run format="text"}
m = 2 * d
print('The total mass is {:.2f} $m^3$'.format(m))
```

The total mass is 2000.00 $m^3$

A runnable code with print statement hiding the code block
----------------------------------------------------------

Run a python code and show the print output, but hiding the code.

Syntax: {.python .run format=\[blockquote (default),
text\] hide\_code=\[False, True\]}

> Output:
>
> > Variable d is 1000.0

A runnable inline code with print statement
-------------------------------------------

It will replace the inline code by the print function output

Syntax: \`(print(code))\`{.run}

Obs: It is returned the raw string (math mode will not work)

Water density is 1000.0 $kg/m^3$ and the total mass was 2000.00 \$m\^3\$

A runnable code with figure generation
--------------------------------------

It will run the code and save the created pyplot figure to a file, than
it creates a Image text block to load it.

Syntax: {.python .run format=\[blockquote (default),
text\] hide\_code=\[False, True\] caption="" label="" width=""}}

-   If more than one figure is created the configuration keyvals can be
    added, such as: caption2="" label2="" width2="" ext2="" ...
-   Figure is saved to folder `./plt-images`

``` {.python .run caption="Figure Number One" label="my_fig"}
from matplotlib import pyplot as plt
plt.plot([1, 2], [3, 4], 'dr-')
```

![Figure Number One](plt-images\8b8e2c026d094d38ae394728b55cdfa02e5687a2.png)

End
