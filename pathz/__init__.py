import os

def join(*parts):
    return os.path.expanduser(os.path.join(*parts))

def exists(path):
    return os.path.exists(os.path.expanduser(path))

def abspath(path):
    return os.path.abspath(os.path.expanduser(path))

