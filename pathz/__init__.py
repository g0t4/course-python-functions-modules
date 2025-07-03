import os

def expand_tilde_first_and_then(path_func):

    def wrapped_path_func(first_component, *parts):
        expanded_component = os.path.expanduser(first_component)
        return path_func(expanded_component, *parts)

    return wrapped_path_func

@expand_tilde_first_and_then
def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        os.stat(path)
    except (OSError, ValueError):
        return False
    return True

join = expand_tilde_first_and_then(os.path.join)
abspath = expand_tilde_first_and_then(os.path.abspath)
# exists = expand_tilde_first_and_then(os.path.exists)

#
# def join(first_component, *parts):
#     expanded_arg = os.path.expanduser(first_component)
#     return os.path.join(expanded_arg, *parts)
#
# def exists(first_component):
#     expanded_arg = os.path.expanduser(first_component)
#     return os.path.exists(expanded_arg)
#
# def abspath(first_component):
#     expanded_arg = os.path.expanduser(first_component)
#     return os.path.abspath(expanded_arg)
#
