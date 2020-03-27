# Options

## Using Classes

- Document 
    - signature, pipe delim
    - description (docstring and attr)
    - init method parameters
    - handle method
    - extending the option class

## Using Functions

You also have the ability to register options that use functions for the handler. The 
only notable difference is how you register the option(s). Instead of passing a list of 
options, simply pass a dictionary where the key will be the option signature. If you would
like to display an option help message, simply use a standard docstring. See below for an 
example:

```python
from cliff import Application

def functionBasedOption(app):
    """Show a quick litte help message"""

    print("\nTODO\n")

Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerOptions({
    '--f|--flag': functionBasedOption
}).run()
```

```bash
Example App                                      v1.0.0
-------------------------------------------------------
This is an example CLI app.

Usage: app.py [option/command]

Options:
  --f|--flag  Show a quick litte help message
```