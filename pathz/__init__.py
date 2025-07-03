import os

def join(first_arg, *parts):
    first_arg = os.path.expanduser(first_arg)
    return os.path.join(first_arg, *parts)

def exists(first_arg):
    first_arg = os.path.expanduser(first_arg)
    return os.path.exists(first_arg)

def abspath(first_arg):
    first_arg = os.path.expanduser(first_arg)
    return os.path.abspath(first_arg)

