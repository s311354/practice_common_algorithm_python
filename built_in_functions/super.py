#!/usr/bin/env python3
#
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
#
# The techniques shown below assure that super() calls a method that is known 
# to exist and that the signature will be correct; however, we're still 
# replying on super() being called at each step so that the chain of delegation
# continues unbroken. This is easy to achieve if we're designing the classes 
# cooperatively - just add a super() call to every method in the chain.
#
# The technique provide the means to design cooperative classes that can be
# composed or reordered by subclasses.
# ==============================================================================

class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')


class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()


class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('Drawing at position:', self.x, self.y)


class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)

    def draw(self):
        self.movable.draw()
        super().draw()


class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass


def main():
    """docstring for main"""
    cs = ColoredShape(color='red', shapename='circle')

    cs.draw()

    print(" === MovableColoredShape === ")

    mcs = MovableColoredShape(color='red', shapename='triangle',
                              x=10, y=20)

    mcs.draw()


if __name__ == '__main__':
    main()
