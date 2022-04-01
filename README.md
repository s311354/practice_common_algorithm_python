# practice_common_algorithm_python
Recap Python basic algorithm

#### Top-level Script Environment ####

'__main__' is the name of the scope in which top-level code executes. A module's __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the main scope by checking its own __name__, which allows a common idiom for conditionallu executing code in a module when it is run as a script or with python -m but not when it is imported.

```
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

#### __name__ Attributes ####

The __name__ attributes must be set to the fully-qualified name of the module. This name is used to uniquely identify the module in the import system.

#### String module ####

The constants defined in this module:
- string.punctuation: String of ASCll characters which are considered punctuation characters in the c locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
- ...

#### Statistics - Mathematical Statistics Functions ####

This module provides functions for calculating mathematical statistics of numeric (Real-value) data.

The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

Functions details:
- statistics.mean(data): Return the sample arithmetic mean if data which can be a sequence or iterable.

#### Random - Generate pseudo-random numbers ####

This module implements pseudo-random number gennerators for various distributions.

#### Built-in Functions ####

The Python interpreter has a number of functions and types built into it that are always available, such as:
- ord(c): Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') return the integer 97
- super([type[, object-or-type]]): Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. The search order is same as that used by getattr() except that the type itself is skipped.
- hasattr(object, name): The arguments are an object and a string. The result is True if the string is the name of one of the object's attributes, False if not.
- gatattr(object, name[, default]): Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object's attributes, the result is the value of that attribute.

Note:
- super() is in the business of delegating method calls to some class in the instance's ancestor tree. For reordered method calls to work, the classes need to be designed coorperatively. 

Please check the [`super.py`](./built_in_functions/super.py) for details.

#### Data model ####

Objects are Python's abstraction for data. All data in a Python program is represented by objects or by relations between objects. Every object has an identity, a type and a value. An object's identity never changes once it has been created.

The built-in types object:
- object.__init__(self[, ...]): called after the instance has been created. but before it is returned to the caller. The arguments are those passed to the class constructor expression.
- object.__repr__(self): built-in function to compute the "official" string represention of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value.
- object.__str__(self): called by str(object) and the built-in functions format() and print() to compute the "informal" or nicely printable string represention of an object. The return value must be a string object.
- object.__len__(self): called to implement the built-in function len(). Should return the length of the object, an integer >= 0. Also, an object that doesn't define a __bool__() method and whose __len__() method retruns zero is considered to be false in a Boolean context.

#### Simple Statements ####

A simple statement is comprised within a single logical line. Several simple statements may occur on a single line separated by semicolons. The syntax for simple statements is:

- pass_stmt ::=  "pass": pass is a null operation, when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code need to be executed.
- yield_stmt ::=  yield_expression: A yield statement is semantically equivalent to a yield expression. The yield statement can be used to omit the parenthesses that would otherwise be required in the equivalent yield expression statement. The yield expression is used when defining a generator function or an asynchronous generator function and thus can only be used in the body of a function definition.

#### Dijkstra's Algorithm ####

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes, but a more common variant fixes a single node as the "source" node and finds shortest path from the source to all other nodes in the graph, producing a shortest-path tree.

#### Container Datatypes ####

This module implements specialized container datatypes providing alternatives to python's general purpose built-in container, dict, list, set, and tuple.
- class tuple([iterable]): Tuples may be constructed in a number of ways, using a pair of parenthesses to denote the empty tuple, using a trailing comma for a singleton tuple: a, or (a,), separating items with commas: a, b, c or (a, b, c), using the tuple() built-in



## Reference ##

- [Automatic documentation generation from code](https://www.sphinx-doc.org/en/master/tutorial/automatic-doc-generation.html)
- [Python: Top-level script environment](https://docs.python.org/3.9/library/__main__.html?highlight=__main__)
- [5.4.4. Import-related module attributes](https://docs.python.org/3.9/reference/import.html?highlight=_name__#import-related-module-attributes)
- [String - Common string operations](https://docs.python.org/3.9/library/string.html?highlight=string.punctuation#string.punctuation)
- [Statistics — Mathematical statistics functions](https://docs.python.org/3.9/library/statistics.html?highlight=scipy)
- [SciPy Documentation](https://scipy.github.io/devdocs/index.html)
- [Random - Generate pseudo-random numbers](https://docs.python.org/3.9/library/random.html?highlight=random#module-random)
- [Built-in Functions: ord](https://docs.python.org/3.9/library/functions.html?highlight=ord#ord)
- [Python: 3. Data model](https://docs.python.org/3/reference/datamodel.html?highlight=__str__#object.__str__)
- [Built-in Functions: super](https://docs.python.org/3.7/library/functions.html#super)
- [Guide to using supr()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/ )
- [Simple Statements](https://docs.python.org/3.7/reference/simple_stmts.html)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Container Datatypes](https://docs.python.org/3.7/library/collections.html#module-collections)
