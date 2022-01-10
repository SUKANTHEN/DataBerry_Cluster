"""
Custom functions
"""
def unique(sequence):
    seen = set()
    x = [x for x in sequence if not (x in seen or seen.add(x))]
    return x

def set_list_convertor(set):
    return [*set, ]

def nan_none_validator(var):
    if (var is None) or (var == ""):
        var = "False"
    elif var != var:
        var = "False"
    else:
        var = var
    return var
