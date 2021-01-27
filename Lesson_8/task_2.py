# 2) Закодируйте любую строку по алгоритму Хаффмана.


from collections import Counter
from binarytree import Node


def walk(node, code_tuple, res: str):
    if node.right is None and node.left is None:
        for t in code_tuple:
            if t[0] == code_tuple[node.val][0]:
                code_tuple[t[1]] = (t[0], res)
    else:
        walk(node.left, code_tuple, res + '0')
        walk(node.right, code_tuple, res + '1')


def encode(s):
    h = Counter(s).items()
    array = sorted(h, key=lambda x: x[1])

    encoded_symbols = []
    for ind, tup in enumerate(array):
        encoded_symbols.append((tup[0], ind))

    while len(array) > 1:
        root = array[0][1] + array[1][1]

        new_node = Node(root)

        if isinstance(array[0][0], Node):
            new_node.left = array[0][0]
        else:
            for tup in encoded_symbols:
                if tup[0] == array[0][0]:
                    new_node.left = Node(tup[1])

        if isinstance(array[1][0], Node):
            new_node.right = array[1][0]
        else:
            for tup in encoded_symbols:
                if tup[0] == array[1][0]:
                    new_node.right = Node(tup[1])

        array.append((new_node, root))

        array = sorted(array, key=lambda x: x[1])
        array = array[2:]

    tree = array[0][0]

    # print(tree)

    walk(tree, encoded_symbols, "")
    return encoded_symbols


print(encode("cheers!"))
