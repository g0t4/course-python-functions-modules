import os

def join(first_component, *parts):
    expanded_arg = os.path.expanduser(first_component)
    return os.path.join(expanded_arg, *parts)

def exists(first_component):
    expanded_arg = os.path.expanduser(first_component)
    return os.path.exists(expanded_arg)

def abspath(first_component):
    expanded_arg = os.path.expanduser(first_component)
    return os.path.abspath(expanded_arg)

