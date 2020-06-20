import os
from cliff import Application


def config():
    """Global access to application config"""

    return Application().config()


def env(key, default=None):
    """Global access to getenv"""

    return default if os.getenv(key) == None else os.getenv(key)
