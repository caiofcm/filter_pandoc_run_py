import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='filter_pandoc_run_py',
      version='0.1',
      description='Run python code from a markdown file and output print or images it',
      long_description=read('README.md'),
      url='To do',
      author='Caio Marcellos',
      author_email='caiocuritiba@gmail.com',
      license='MIT',
      packages=find_packages(),
     install_requires=['pandocfilters', 'matplotlib'],
      keywords='pandoc filters markdown python notes',
      zip_safe=False,
      py_modules=["filter_pandoc_run_py.filter_pandoc_run_py"],
      entry_points={
          'console_scripts': [
              'filter_pandoc_run_py = filter_pandoc_run_py.filter_pandoc_run_py:main',
          ],
      },
      extras_require={
          'dev': ['check-manifest'],
          'test': ['coverage'],
      },
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'coverage'],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: BSD License", #to be reviewed
      ]

      # Alternatively, if you want to distribute just a my_module.py, uncomment
      # this:
)
