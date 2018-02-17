
# Executing python codes in a markdown file


## Cases without printing

### Regular block code

A regular markdown code definition

Syntax: \{.python}

```{.python }
e = 'foo'
```

### A runnable block code

For a runnable code append the class .run

Syntax: \{.python .run}

```{.python .run}
d = 1e3
```

### A runnable inline code

An inline code can also be run in python.

Syntax: \`(code)\`\{.run\}

Code to run is `foo = 1`{.run}.

## Cases with printing

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

### A runnable code with print statement hiding the code block

Run a python code and show the print output, but hiding the code.

Syntax: \{.python .run format=[blockquote (default), text]\ hide_code=[False, True]}

```{.python .run hide_code=True}
m = 2 * d
print('Variable d is {}'.format(d))
```

### Printing a string from python having markdown syntax

Syntax: \{.python .run format=[text]\}

```{.python .run format=text}
a = '5.0 $\\frac{kg}{m^3}$'
b = 1.0
## table can be obtained from a lib such as tabulate 

s = '''
A | B |
---- | ---- |
{} | {} $\\frac{{kg}}{{m^3}}$ |
'''.format(a, b)

print(s)
```

### A runnable inline code with print statement

It will replace the inline code by the print function output

Syntax: \`(print(code))\`\{.run\}

Obs: It is returned the raw string (math mode will not work)

Water density is `print(d)`{.run} $kg/m^3$ and the total mass was `print('{:.2f} $m^3$'.format(m))`{.run}

## Figures generation

### A runnable code with one figure generation

It will run the code and save the created pyplot figure to a file, than it creates a Image text block to load it.

Syntax: \{.python .run format=[blockquote (default), text]\ hide_code=[False, True] caption="" label="" width=""}}

- Uses _pandoc-fignos_ filter notation for caption, label and width.
- If more than one figure is created the configuration keyvals can be added, such as: caption2="" label2="" width2="" ext2="" ...
- Figure is saved to folder `./plt-images`

```{.python .run caption="Figure Number One" label="my_fig"}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
plt.plot([1, 2], [3, 4], 'dr-')
```

### A runnable code with two figures generation

It will run the code and save the created pyplot figure to a file, than it creates a Image text block to load it.

Syntax: \{.python .run format=[blockquote (default), text]\ hide_code=[False, True] caption="" label="" width=""}}

- Uses _pandoc-fignos_ filter notation for caption, label and width.
- If more than one figure is created the configuration keyvals can be added, such as: caption2="" label2="" width2="" ext2="" ...
- Figure is saved to folder `./plt-images`

```{.python .run caption="Number One" caption2="Other Figure" label="my_fig" label2="my_fig2"}
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

## Non filter related tests

### Math expression

Oi math $\dfrac{1}{2} - a^2 = 2$