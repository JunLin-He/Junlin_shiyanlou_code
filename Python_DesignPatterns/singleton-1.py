# -*- coding: utf-8 -*-

class Singleton(object):
    """
    Singleton mode
    """
    class _A(object):
        """
        The working class, hides from the outside
        """ 
        def __init__(self):
            pass

        def display(self):
            """ return the globle unique ID of current instance """
            return id(self)

    # class variable, for storing the instance of _A
    _instance = None

    def __init__(self):
        """
        Determine if the instance of _A has been saved in the class variable first,
        if not, create one and return
        """
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()

    def __getattr__(self, attr):
        """
        All properties should be obtained from Singleton._instance directly
        """
        return getattr(self._instance, attr)


if __name__ == '__main__':
    # Create two instances
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), s1.display())
    print(id(s2), s2.display())