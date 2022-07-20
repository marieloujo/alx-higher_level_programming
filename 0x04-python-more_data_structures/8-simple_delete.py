#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except Exception:
        pass
    finally:
        return a_dictionary
