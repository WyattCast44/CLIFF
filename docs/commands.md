# Commands

The primary differnce between commands and options is that options are parsed first.

## Using Classes

- Document 
    - signature, pipe delim
    - description (docstring and attr)
    - init method parameters
    - handle method
    - extending the option class

## Using Functions

You also have the ability to register commands that use functions for the handler. The 
only notable difference is how you register the command(s). Instead of passing a list of 
classes, simply pass a dictionary where the key will be the command signature. If you would
like to display an command help message, simply use a standard docstring. See below for an 
example:

```python
from cliff import Application

def functionBasedCommand(app):
    """Show a quick litte help message"""

    print("\nTODO\n")

Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerCommands({
    'my:command': functionBasedCommand
}).run()
```

```bash
Example App                                      v1.0.0
-------------------------------------------------------
This is an example CLI app.

Usage: app.py [option/command]

Commands:
  my:command  Show a quick litte help message
```

### Working with Parameters

The function must accept an instance of the application as the first parameter
Any parameters after that will be parsed and used as required parameters, unless you 
set a default value. See below for an example:

```python
from cliff import Application

def sayHello(app, name, greeting="Hello,"):
    """Show a quick litte help message"""

    print(f"\n{greeting} {name}")

Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerCommands({
    'say:hello': sayHello
}).run()
```