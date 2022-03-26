class Node:
    """description"""
    def __init__(self, data=None, next=None):
        self.data_ = data
        self.next_ = next

    def get_data(self):
        """docstring for get_data"""
        return self.data_

    def set_data(self, data):
        """docstring for set_data"""
        self.data_ = data

    def get_next(self):
        """docstring for get_next"""
        return self.next_
    
    def set_next(self, next):
        """docstring for set_next"""
        self.next_ = next

    def __str__(self):
        return str(self.data_)
