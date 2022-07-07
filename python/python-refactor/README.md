# Refactoring Python 2 code to Python 3 with 2to3
This batch change is an example of how to use `2to3` to refactor Python 2 code into Python 3. The Python docs have [more information on 2to3](https://docs.python.org/3/library/2to3.html). This will:

- Find repositories using Python 2-style print statments, with Python-language files in them.
- Install `2to3` in the container.
- Run `2to3` on the respositories that Sourcegraph finds.

## How to
- If running this issue on your own code, you may want to adjust the `repositoriesMatchingQuery` to just look for repositories containing Python code, rather than using the Python 2-style print statement as an indicator of Python 2 code. You may also want to adjust the repository exclusions (`-repo:python-language-server -repo:ctags`) to meet your needs, and may wish to exclude forks by removing `fork:yes`. 

# More info
For more info on how Sourcegraph can help you find Python 2 code in your codebase, please review our [Refactor Python 2 to 3 example repos](https://sourcegraph.com/refactor-python2-to-3).