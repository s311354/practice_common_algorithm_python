#!/usr/bin/env python3
"""
A simple module for printing "Array"

.. module:: Array

.. moduleauthor:: Amo

"""


def array_test():
    """This function prints hello with a name

    Args:
       name (str):  The name to use.

    Returns:
       int.  The return code::

          0 -- this always return 0

    Raises:
       AttributeError, KeyError

    A really simple function. Really!

    >>> print_hello_with_name('foo')
    Hello, foo

    """
    ar = [3, 2, 4, 5]

    __import__('pprint').pprint(ar)
    ar.pop()
    ar.append(6)

    __import__('pprint').pprint(ar)

    __import__('pprint').pprint("Index of 4: %s " % ar.index(4))

    ar.remove(4)

    __import__('pprint').pprint(ar)

    ar.reverse()
    __import__('pprint').pprint(ar)
    __import__('pprint').pprint(sorted(ar))

    ar.sort()
    __import__('pprint').pprint(ar)


def main():
    array_test()


if __name__ == "__main__":
    main()
