import filter_pandoc_run_py
import json
from pandocfilters import applyJSONFilters

def test_inline_plot_mpl_multiples():
	MD_SAMPLE = '''

# Creates Three figures Matplotlib figure

```python
#filter: {.run caption="Figure Number One" label="my_fig" hide_code=true title_as_caption=true figattr="#fig:1 width=5in"}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt
plt.figure()
plt.plot([1, 2], [-1, -4], 'or-')
plt.title('This is figure caption from python')
```

```{.python .run caption="Second Figure" caption2="Third Figure" label="my_fig_2" label2="my_fig_3" hide_code=true figattr="#fig:2 width=8in" figattr2="#fig:3 width=3in tag='B.1'"}
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


'''
	ast_string = filter_pandoc_run_py.run_pandoc(MD_SAMPLE)
	processed = applyJSONFilters(
        [filter_pandoc_run_py.run_py_code_block], ast_string
    )
	d = json.loads(processed)
	assert d['blocks'][1]['c'][0]['t'] == 'Image'

def insider_Debugger():
	test_inline_plot_mpl_multiples()
	pass

if __name__ == '__main__':
	insider_Debugger()
	pass    


#filter: {.run caption="Second Figure" caption2="Third Figure" label="my_fig_2" label2="my_fig_3" hide_code=true captions=['cap1', 'cap2']}
