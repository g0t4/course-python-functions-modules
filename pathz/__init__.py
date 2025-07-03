import os

def join(first_arg, *parts):
    return os.path.expanduser(os.path.join(first_arg, *parts))

def exists(path):
    first_arg = os.path.expanduser(path)
    return os.path.exists(first_arg)

def abspath(path):
    first_arg = os.path.expanduser(path)
    return os.path.abspath(first_arg)

