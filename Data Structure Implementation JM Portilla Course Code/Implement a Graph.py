from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited = 1  # White
    visited = 2  # Black
    visiting = 3  # Gray

class Node(object):

    def __init__(self,num):
        self.num = num
        self.adjacent = OrderedDict()
        self.visit_state = State.unvisited

    def __str__(self):
        return str(self.num)

class Graph(object):

    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self,source,dest, weight = 0):

        if source not in self.nodes:
            add_node(source)
        if dest not in self.nodes:
            add_node(dest)

        self.nodes[source].adjacent[self.nodes[dest]] = weight


