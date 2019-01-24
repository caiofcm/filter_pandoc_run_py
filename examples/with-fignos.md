---
fignos-cleveref: True
fignos-plus-name: Fig.
header-includes: \usepackage{caption}
...

Reference to @fig:1.

![The number one.](plt-images/8f1a04c1b6419e08455f95cd1f28cfa7bddf2caa.png){#fig:1 width=5in}

![The number two.](plt-images/../../plt-images/8f1a04c1b6419e08455f95cd1f28cfa7bddf2caa.png){#fig:2 width=5in}

*@fig:2 is given above.

![The number three.](plt-images/b59b4a1518715d260505263dcf0fe4bc375bdcae.png){#fig: width=1in}

```python
#filter: {.run caption="Figure Number One" label="my_fig" hide_code=true title_as_caption=true}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
plt.figure()
plt.plot([1, 2], [-1, -4], 'or-')
plt.title('This is figure caption from python')
```

```python
#filter: {.run caption="Second Figure" caption2="Third Figure" label="my_fig_2" label2="my_fig_3" hide_code=true}
# import matplotlib
# matplotlib.use('AGG')
# from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# First Figure
plt.figure()
plt.plot([1, 2], [3, 4], 'dg-')


fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)
```

