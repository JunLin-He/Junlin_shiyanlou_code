# -*- coding: utf-8 -*-

class Singleton:
    """
    Singleton class decorator can be used to implement any class of singleton case.
    But it can't be multiple threading environment.
    """

    def __init__(self, cls):
        """ The command parameter is a class """
        self._cls = cls

    def Instance(self):
        """
        Return the true instance
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


# Decorator
@Singleton
class A:
    """ A class that need singleton mode """
    def __init__(self):
        pass

    def display(self):
        return id(self)

if __name__ == '__main__':
    s1 = A.Instance()
    s2 = A.Instance()
    print(s1, s1.display())
    print(s2, s2.display())
    print(s1 is s2)