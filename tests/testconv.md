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

Figures generation
------------------

\$ A runnable code with one figure generation
---------------------------------------------

It will run the code and save the created pyplot figure to a file, than
it creates a Image text block to load it.

Syntax: {.python .run format=\[blockquote (default),
text\] hide\_code=\[False, True\] caption="" label="" width=""}}

-   Uses *pandoc-fignos* filter notation for caption, label and width.
-   If more than one figure is created the configuration keyvals can be
    added, such as: caption2="" label2="" width2="" ext2="" ...
-   Figure is saved to folder `./plt-images`

``` {.python .run caption="Figure Number One" label="my_fig"}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
plt.plot([1, 2], [3, 4], 'dr-')
```

![Figure Number One](plt-images\fee4b8909259e13196aa045e1cf64c47d0e78936.png)

### A runnable code with two figures generation

It will run the code and save the created pyplot figure to a file, than
it creates a Image text block to load it.

Syntax: {.python .run format=\[blockquote (default),
text\] hide\_code=\[False, True\] caption="" label="" width=""}}

-   Uses *pandoc-fignos* filter notation for caption, label and width.
-   If more than one figure is created the configuration keyvals can be
    added, such as: caption2="" label2="" width2="" ext2="" ...
-   Figure is saved to folder `./plt-images`

``` {.python .run caption="Number One" caption2="Other Figure" label="my_fig" label2="my_fig2"}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# First Figure
plt.plot([1, 2], [3, 4], 'dr-')

# Second Figure
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)
```

![Number One](plt-images\df0e1093ac26eab2a07f0ad913f647d4a059aa33.png)

![Other Figure](plt-images\1eb0e55a6a6482e392ae4291ec26e96b9ae79cbb.png)

End
