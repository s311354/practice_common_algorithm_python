Recap Python basic algorithm

#### Top-level Script Environment ####

'__main__' is the name of the scope in which top-level code executes. A module's __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the main scope by checking its own __name__, which allows a common idiom for conditionallu executing code in a module when it is run as a script or with python -m but not when it is imported.

```
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

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
- enumerate(iterable, start=0): Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.


Note:
- super() is in the business of delegating method calls to some class in the instance's ancestor tree. For reordered method calls to work, the classes need to be designed coorperatively. 

Please check the [`super.py`](./built_in_functions/super.py) for details.

#### Built-in Types ####

The principal built-in types are numerics, sequences, mappings, classes, instances, and expecptions.

Here are most of the built-in objects considered false:
+ constants defined to be false: None and False
+ zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
+ empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True, unless otherwise stated.

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


**Dictionaries can be created by several means**
- class dict(** kwargs) dictionaries can be created by several mean:
    - Use a comma-separated list of key: value pairs within braces: {'jack': 4098, 'sjoerd': 4227}
    - Use a dict comprehension: {}
    - Use the type constructor: dict()

**Sets can be created by several means**
- Use a comma-separated list of elements within braces: {'jack', 'sjoerd'}
- Use a set comprehension: {c for c in 'abrace' if c not in 'abc'}
- Use the type constructor: set(), set('foobar')

## Factory Function for Truples with Named Fields ##

Named tuple assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of poistion index.

```
>>> # Basic example
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
>>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
```

Named tuples are especially useful for assigning field names to result tuples returned by the csv modules:

```
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)
```

#### queue - A synchronized queue class ####

The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when information must be exchanged safely between multiple thread. The Queue class in this module implements all the required locking semantics. The queue module defines the following classes and exceptions:
- class queue.Queue(maxsize = 0): constructor for a FIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue.
- class queue.LifoQueue: constructor for a LIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will bolck once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.


#### sys - System-specific parameters and functions ####
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

- sys.getsizeof(object[, default]): Return the size of an object in bytes. The object can be any type of object.

#### Lambda Expressions ####

Small anonymous function can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used whenever function are required. They syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition.

Here is the like nested function definitions
```
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

Here is another use for passing a small function as an argument:
```
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

#### Unit Testing Framework ####

The unittest unit testing framework was originally inspired by JUit and has a similar flavor as major unit testing framework in other language. It supports test automation, sharing of setup and shut-down code for tests. aggregation of tests into collections, and independence of the tests from the reporting framework.

To achieve this, unittest supports some inportant concepts in an object-oriented way:
+ test fixture - a test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
+ test case - A test case is ths individual unit of testing. It checks for a specifc response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
+ test suite - A test suite is a collection of test cases, test suites, or both. It is used aggregate tests that should be executed together.
+ test runner - A test runnner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

The TestCase class provides several assert methods to check for and report failures.

|  Method      |    Check that       |  New in   	|
| ------------- |-------------  | ------- |
|    assertEqual(a, b)    |    a == b          |        |
|    assertNotEqual(a, b)    |    a != b          |        |
|    assertTrue(x)    |    bool(x) is True          |        |
|    assertFalse(x)    |    bool(x) is False          |        |
|    assertIs(a, b)    |    a is b          |        |
|    assertIsNot(a, b)    |    a is not b          |        |
|    assertIsNone(x)    |    x is None          |        |
|    assertIsNotNone(x)    |    x is not None          |        |
|    assertIn(a, b)    |    a in b          |        |
|    assertNotIn(a, b)    |    a not in b          |        |
|    assertIsInstance(a, b)    |    isinstance(a, b)          |        |
|    assertNotIsInstance(a, b)    |   not isinstance(a, b)          |        |


#### Higher-order Functions and Operations on callable Objects ####

@functools.lru_cache(user_function): least recently used cache

Decorator to wrap a function with a memoizinf callable that saves up to the maxsize most recent calls. It can save time when expensive or I/Q bound function is periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.

Distinct arguments patterns may be considered to be distinct calls with separate cache entries.


#### Function Annotations ####




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
- [queue - A synchronized queue class](https://docs.python.org/3/library/queue.html?highlight=lifoqueue#queue.LifoQueue)
- [sys - System-specific parameters and functions](https://docs.python.org/3/library/sys.html?highlight=getsizeof#sys.getsizeof)
+ [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
+ [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#more-control-flow-tools)
+ [Unit testing framework](https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest)
+ [functools - Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html#functools.lru_cache)
+ [PEP 3107 – Function Annotations](https://peps.python.org/pep-3107/)
