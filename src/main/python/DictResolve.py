import unittest

'''
Challenge #226:
This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
'''


class DResolveTest(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)
        self.assertEqual(dict_resolve(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']), ['x', 'z', 'w', 'y'])
        self.assertEqual(dict_resolve(['xcp', 'wcp', 'cxl', 'ccx', 'cpl', 'cpw']), ['x', 'l', 'w', 'c', 'p'])


class DNode:

    def __init__(self, value=None):
        self.value = value

        # children_map and children_list used to create ordered map
        self.children_map = {}
        self.children_list = []

    def add(self, data, index=0):
        if len(data) > index:
            child_key = data[index]
            if child_key in self.children_map:
                nd = self.children_list[self.children_map[child_key]]
            else:
                nd = DNode(child_key)
                self.children_map[child_key] = len(self.children_list)
                self.children_list.append(nd)

            nd.add(data, index + 1)

    def generate_resolve_tree(self, tree):
        lst = self.children_list

        for src, dest in zip(lst, lst[1:]):
            src_node = tree.get_node(src.value)
            dest_node = tree.get_node(dest.value)
            src_node.add_edge(dest_node)

        for child in lst:
            child.generate_resolve_tree(tree)


class ResolveNode:

    def __init__(self, value=None):
        self.value = value
        self.edges = {}
        self.dist = 0

    def add_edge(self, node):
        self.edges[node.value] = node


class ResolveNodeContainer:
    def __init__(self):
        self.nodes = {}

    def get_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = ResolveNode(value)

        return self.nodes[value]


def dict_resolve(data):
    root = DNode()

    for w in data:
        root.add(w)

    resolve_nodes = ResolveNodeContainer()

    root.generate_resolve_tree(resolve_nodes)

    nodes = list(resolve_nodes.nodes.values())

    while len(nodes) > 0:
        node = nodes.pop()
        for child in node.edges.values():
            if child.dist < node.dist + 1:
                child.dist = node.dist + 1
                nodes.append(child)

    nodes = list(resolve_nodes.nodes.values())
    nodes = sorted(nodes, key=lambda n: n.dist)

    return [x.value for x in nodes]


if __name__ == '__main__':
    unittest.main()
