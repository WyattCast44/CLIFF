# Options

The intented use of options in CLIFF are as flags to your application. 
For example, you might use a `--quiet` option to silence all print/output 
from your application. You would still need to implement the checks in your 
commands to ensure the options intended effects are accomplished. 

You have several ways you define and register your application options, see below for 
additional details.

## Options Quickstart

All options need a handler, which can be either a function or a class. Once you have created your handler
all you need to do is register it with your application using the `registerOptions()` method.

```python
Application().registerOptions(
    # You option handlers here :)
).run()
```

## Options Signature Rules

- Signatures names must be comprised of lowercase characters and digits
- All options must be preceded by either a single of double hyphen (-, or --)

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

## Pre-Built Options

CLIFF has several built in options that you can use in your application
if you so desire. See below for a complete list and examples.

### The Quiet Option

The pre-built `Quiet` option is a simple flag that users can pass 
if they would like all output by the application to be hidden. It works by intercepting any calls to `sys.stout` and silently bypassing them.

If you need to build checks into your custom commands, you can use the  application's `is_quiet()` method which will return true if the quiet flag has been passed.

```python
from cliff import Application
from cliff.options import Quiet

Application().registerOptions([
    Quiet
]).run()

if self.app.is_quiet():
    # do something, but do it silently...
```