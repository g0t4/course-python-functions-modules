import os

def join(*parts):
    return os.path.expanduser(os.path.join(*parts))

def exists(path):
    first_arg = os.path.expanduser(path)
    return os.path.exists(first_arg)

def abspath(path):
    first_arg = os.path.expanduser(path)
    return os.path.abspath(first_arg)

