import os

def join(first_arg, *parts):
    expanded_arg = os.path.expanduser(first_arg)
    return os.path.join(expanded_arg, *parts)

def exists(first_arg):
    expanded_arg = os.path.expanduser(first_arg)
    return os.path.exists(expanded_arg)

def abspath(first_arg):
    expanded_arg = os.path.expanduser(first_arg)
    return os.path.abspath(expanded_arg)

