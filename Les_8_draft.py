from collections import Counter
from heapq import heappush, heappop


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class Tree:
    def __init__(self, some_str):
        self.root = None
        self.some_str = some_str

    def get_node(self, data, left, right):
        return Node(data, left, right)

    def count(self):
        user_str = Counter(self.some_str)
        counted_str = user_str.most_common()[:-len(user_str) - 1:-1]
        return counted_str

    def create_node(self):
        h = []
        for i, j in d.count():
            h.append((j, len(h), i))

        count = len(h)
        print(h)
        while len(h) > 1:
            freq1, _count1, left = heappop(h)
            freq2, _count2, right = heappop(h)

            heappush(h, (freq1 + freq2, count, Node(left=left, right=right)))
            count += 1
        print(h)
        a = Node()
        print(a.right)


d = Tree('beep boop beer!')

print(d.count())

h = []
for i, j in d.count():
    h.append((j, i))

count = len(h)
print(h)
while len(h) > 1:
    preor1, left = heappop(h)
    preor2, right = heappop(h)
    d.root = d.get_node(preor1 + preor2, left, right)

    heappush(h, (preor1 + preor2, left + right))
    count += 1
print(h)
print(d.root.data)


# a = []
# b = []
# #
# i = 0
# j = 1
# #
# for num in range(len(d.count())):
#     if i == len(d.count()) - 1:
#         a.append(d.count()[i][1])
#         b.append(d.count()[i][0])
#         break
#     a.append(d.count()[i][1] + d.count()[j][1])
#     b.append(d.count()[i][0] + d.count()[j][0])
#     i += 2
#     j += 2
#
# #     # print(type(el))
# #     # print(el[i])
# #     # a.append(el[i])
# #     # print(el)
#
# print(a)
# print(b)
# print(d.count())
# print(len(d.count()))
# print(d.count()[4] + d.count()[5])
