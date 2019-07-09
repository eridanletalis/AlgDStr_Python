from collections import Counter


class Node:
    def __init__(self, freq, val=None, left=None, right=None):
        self.freq = freq
        self.val = val
        self.left = left
        self.right = right


def huffman(_string):
    counts = Counter(_string)
    print(counts)
    Nd = []
    item, val = counts.popitem()
    Nd.append(Node(val, item))
    item, val = counts.popitem()
    Nd.append(Node(val, item))
    Nd = Node(Nd[0].freq + Nd[1].freq, None, Nd[0], Nd[1])
    print(Nd)
    print(counts)
    counts1 = Counter([Nd]*Nd.freq)
    counts += counts1
    print(counts)
    item, value = counts.popitem()
    print(type(item))
    print(type(value))
    print(type(Node))
    print(type(Node) == type(item))
    print(counts)

s = "beep boop beer!"
code = huffman(s)

