import src.Node


def test():
    """
    Tester function for Node class
    """
    ll = src.Node.Node("First", None)
    ll.append("Second")
    ll.append(3)
    ll.append([1, 2, 3])
    print(ll.pop())
    tmp = ll
    while tmp:
        print(tmp.data)
        tmp = tmp.node


if __name__ == '__main__':
    test()