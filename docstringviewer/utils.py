"""
Main module with application logic
"""
import os
import importlib
import inspect

from .conf import PROJECT_ROOT


def build_tree(folder, result):
    """
    Method returns recursively the tree with relevant information about apps, packages and modules.
    """
    children = sorted(os.listdir(folder), key=lambda x: os.path.isfile(os.path.join(folder, x)))

    # Do not build tree for non python packages
    if '__init__.py' not in children and 'manage.py' not in children:
        return result

    for child in children:
        if not child.startswith('.'):
            full_path = os.path.join(folder, child)

            if os.path.isdir(full_path):
                data = build_tree(full_path, [])
                if data:
                    result.append({'name': child, 'data': data})

            elif child.endswith('.py') and not child.startswith('__'):
                import_path = ".".join(filter(None, os.path.splitext(full_path)[0].replace(PROJECT_ROOT, '').split('/')))
                result.append({'name': child, 'import_path': import_path})

    return result


# Todo: get documentation for module-level and class level variables
def get_module_docs(module_string):
    """
    Returns docs dictionary that contains docs data form module-level variables, functions and classes
    for given module string (e.g. "package1.package2....packageN.module").
    """
    if not module_string:
        return None
    module = importlib.import_module(module_string)
    docs = {
        "module": {
            "name": module.__name__.split('.')[-1],
            "description": inspect.getdoc(module)
        }
    }

    # get module-level vars
    variables = [{"name": name, "value": value} for name, value in inspect.getmembers(module)
                 if not callable(value) and not inspect.ismodule(value) and not name.startswith('_')]
    # get functions
    functions = inspect.getmembers(module, inspect.isfunction)
    docs['functions'] = process_routines(functions, module.__name__)

    # get classes
    classes = inspect.getmembers(module, inspect.isclass)
    docs['classes'] = [get_class_data(cls, name) for name, cls in classes
                       if cls.__module__ == module.__name__ and not name.startswith('_')]

    return docs


def get_var_data(var_obj):
    """
    Returns docs data for module-level variable.
    """
    pass


def process_routines(routines, module_name):
    """
    Returns list of dictionaries that holds routines data (name, description
    arguments).
    """
    return [get_routine_data(routine, name) for name, routine in routines
            if routine.__module__ == module_name and not name.startswith('_')]


def get_routine_data(routine, name):
    """
    Returns docs data for routine (any kind of function or method object).
    """
    return {
        "name": name,
        "description": inspect.getdoc(routine),
        "signature": "%s%s" % (name, get_routine_arguments(routine))
    }


def get_routine_arguments(routine):
    """
    Returns dictionary that contains required, positional, keyword and default arguments
    for given routine.
    """
    args, varargs, varkwargs, defaults = inspect.getargspec(routine)

    builder = []
    if args:
        index = len(args) - len(defaults) if defaults else len(args)

        builder.extend(args[:index])
        if defaults:
            builder.extend(["{0}={1}".format(name, value) for name, value in zip(args[index:], defaults)])
    if varargs:
        builder.append("*%s" % varargs)
    if varkwargs:
        builder.append("**%s" % varkwargs)

    return "(%s)" % ", ".join(builder)


def get_class_data(class_obj, name):
    """
    Returns docs data for module-level class object.
    """
    methods = inspect.getmembers(class_obj, inspect.ismethod)
    return {
        "name": name,
        "description": inspect.getdoc(class_obj),
        "methods": process_routines(methods, class_obj.__module__),
    }
