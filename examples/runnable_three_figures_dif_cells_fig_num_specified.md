
# Creates Three figures Matplotlib figure

```python
#filter: {.run caption="Figure Number One" label="my_fig" hide_code=true title_as_caption=true}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
plt.figure(num=2)
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
plt.figure(num=3)
plt.plot([1, 2], [3, 4], 'dg-')


fig = plt.figure(num=4)
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)
```

