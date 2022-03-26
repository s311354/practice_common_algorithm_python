from node import Node

class LinkedList(object):
    """description"""
    def __init__(self):
        self.head_ = None

    def set_head(self, head_node):
        """docstring for set_head"""
        self.head_ = head_node

    # Pushes an item on the front of the list
    def push(self, value):
        """docstring for push"""
        node = Node(value)
        node.set_next(self.head_)
        self.set_head(node)

    # Pop an item from the front of the list
    def pop(self):
        """docstring for pop"""
        if self.head_:
            self.head_ = self.head_.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    def contain(self, value):
        """docstring for fname"""
        found = False
        current = self.head_

        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()

        return found

    # Append an item on the last of the list
    def append(self, value):
        """docstring for append"""
        node = Node(value)
        current = self.head_

        if not current:
            self.head_ = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)

    # Deletes all instance of given value in list
    def delete(self, value):
        """docstring for delete"""
        current = self.head_
        prev = None

        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head_ = current.get_next()
            else:
                prev = current

            current = current.get_next()

    def __len__(self):
        count = 0
        current = self.head_

        while current:
            count += 1
            current = current.get_next()

        return count

    def __str__(self):
        current = self.head_
        output = ""

        while current:
            output += str(current) + " -> "
            current = current.get_next()

        return output
