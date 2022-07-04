#!/usr/bin/python3
"""Only subclass of """


def inherits_from(obj, a_class):
    """My function inherits_from:checks instance of the object from the inherited directly or indirect
      Args:
          first parameter: obj
          second parameter a_class
      Return :
              a bool value
     """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
