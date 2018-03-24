import types


def hide_key(key, hide=lambda s: s // 2):
    """
    Hide part of the key and return e.g. 'abc***123'.
    """
    key_len = len(key)

    if isinstance(hide, types.FunctionType):
        hide = hide(key_len)

    before = (key_len - hide) // 2 + 1
    after = before + hide

    return key[:before] + '*' * hide + key[after:]
