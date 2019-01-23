
# Creates Two Matplotlib figure

```python
#filter: {.run caption2="Number One" caption3="Other Figure" label2="my_fig_2" label3="my_fig_3"}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# First Figure
plt.plot([1, 2], [3, 4], 'dg-')

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

