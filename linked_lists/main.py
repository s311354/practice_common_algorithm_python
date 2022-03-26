#!/usr/bin/env python3
from linked_list import LinkedList


def main():
    """docstring for main"""
    ll = LinkedList()

    print("Initial size:", len(ll))
    ll.push(24)
    print("New size: ", len(ll))
    ll.push(6)
    ll.push(783)
    print("List content: ", ll)

    print("Does List contain 24?")
    if ll.contain(24):
        print("Yes")
    else:
        print("No")

    print("Deletes 24")
    ll.delete(24)

    ll.append(15)
    print("List content: ", ll)


if __name__ == '__main__':
    main()
