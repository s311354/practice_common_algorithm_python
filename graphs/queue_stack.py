import sys
import queue


def main():
    """docstring for main"""
    print("queue:")

    q = queue.Queue()

    for i in range(15):
        q.put(i)

    while not q.empty():
        print(q.get())

    print("stack:")

    s = queue.LifoQueue()

    for i in range(15):
        s.put(i)

    while not s.empty():
        print(s.get())

    print("integer: ", sys.getsizeof(3))
    print("list: ", sys.getsizeof([4, 12]))


if __name__ == '__main__':
    main()
