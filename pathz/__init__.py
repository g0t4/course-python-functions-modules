import os

def join(*parts):
    return os.path.expanduser(os.path.join(*parts))


