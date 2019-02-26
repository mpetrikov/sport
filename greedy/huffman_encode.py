import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        """code - код, который накопили, дойдя до заданного листа или узла"""
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    # строим дерево снизу, выбирая элементы с самым низким приоритетом
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1


    code = {}

    if h:
        # последний оставшийся элемент - корень дерева
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

def huffman_decode(encode, code):
    #primitive, without tree
    result = ''
    keys = code.keys()
    while len(encode) > 0:
        for k in keys:
            if encode[:len(k)] == k:
                result += code[k]
                encode = encode[len(k):]

    return result

def main():
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

    print('huffman_decode', huffman_decode("01001100100111", {'0': 'a', '10': 'b', '110': 'c', '111': 'd'}))

def test(n_iter = 100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s

if __name__ == "__main__":
    main()
