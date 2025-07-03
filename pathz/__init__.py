import os

def new_func_factory(func):

    def new_func(first_component, *parts):
        expanded_arg = os.path.expanduser(first_component)
        return func(expanded_arg, *parts)

    return new_func


join = new_func_factory(os.path.join)
abspath = new_func_factory(os.path.abspath)
exists = new_func_factory(os.path.exists)

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
