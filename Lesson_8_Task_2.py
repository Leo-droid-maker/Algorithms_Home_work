from heapq import heapify, heappush, heappop
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):

    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):

    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heappop(h)
        freq2, _count2, right = heappop(h)
        heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input('Введите строку: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f"{ch}: {code[ch]}")
    print(encoded)


main()