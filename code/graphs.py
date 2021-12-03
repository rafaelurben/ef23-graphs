# ============================================================================= #
# Graphs by https://github.com/rafaelurben/                                     #
#                                                                               #
# Runtime:          Python > 3.10                                               #  
# Dependencies:     python3.10 -m pip install -r requirements.txt               #
# ============================================================================= #

# Imports

import random
from typing import TypeAlias
from rich import print as rprint
from rich.panel import Panel
from rich.console import Group
from rich.pretty import Pretty

WeightType: TypeAlias = float | int
NodeType: TypeAlias = str
EdgeType: TypeAlias = tuple[str, str, WeightType]

# Base classes


class GraphException(TypeError):
    pass


class BaseGraph:
    "A base class for graphs"

    def __init__(self, directed: bool = False, weighted: bool = True, **kwargs):
        self.directed = directed
        self.weighted = weighted
        self.init(**kwargs)

    # Methods subclasses shall overwrite.

    def init(self, **kwargs):
        "Initialize the graph - This method should be overriden in subclasses."

    def get_nodes(self) -> list[NodeType]:
        "Get all nodes - This method has to be overriden in subclasses."
        raise NotImplementedError

    def add_node(self, node: NodeType) -> None:
        "Add a node - This method has to be overriden in subclasses."
        raise NotImplementedError

    def add_edge(self, node1: NodeType, node2: NodeType, weight: WeightType = 0) -> None:
        "Add an edge - This method has to be overriden in subclasses."
        raise NotImplementedError

    def remove_node(self, node: NodeType) -> None:
        "Remove a node - This method has to be overriden in subclasses."
        raise NotImplementedError

    def remove_edge(self, node1: NodeType, node2: NodeType, weight: WeightType = 0) -> None:
        "Remove an edge - This method has to be overriden in subclasses."
        raise NotImplementedError

    def get_neighbors(self, node: NodeType) -> list[EdgeType]:
        "Get all neighbors of a node with their corresponding weight - This method has to be overriden in subclasses."
        raise NotImplementedError

    # Algorithms

    def get_prim_edges(self, startnode: NodeType | None = None) -> list[EdgeType]:
        "Apply prim's algorithm"

        if not self.weighted:
            raise GraphException(
                "Graph must be weighted to be used with the prim algorithm.")

        nodes_all = self.get_nodes()
        nodes_connected = []
        edges_connected = []

        if startnode is not None and startnode not in nodes_all:
            raise GraphException("Startnode has to be in the graph!")

        node_start = startnode or random.choice(nodes_all)
        nodes_connected.append(node_start)

        while len(nodes_all) > len(nodes_connected):
            shortest_connection = None
            shortest_edge = None

            for node in nodes_connected:
                for neighbor, weight in self.get_neighbors(node):
                    if neighbor not in nodes_connected and (shortest_connection is None or weight < shortest_connection):
                        shortest_connection = weight
                        shortest_edge = (node, neighbor, weight)

            if shortest_connection == None:
                raise GraphException(
                    "For prim's algorithm to work, every node has to be connected to the graph!")

            edges_connected.append(shortest_edge)
            nodes_connected.append(shortest_edge[1])
        return edges_connected

    def get_dijkstra_edges(self, startnode: NodeType, endnode: NodeType) -> list[EdgeType]:
        "Apply Dijkastra's algorithm"

        # TODO: Implement Dijkstra's algorithm

    def get_hierholzer_path(self, startnode: NodeType) -> list[NodeType]:
        "Apply Hierholzer's algorithm"

        # TODO: Implement Hierholzer's algorithm

# Different graph storage types


class NodeEdgelistGraph(BaseGraph):
    "Graph type storing the data in nodelists and edgelists"

    def init(self, nodes: list[NodeType] = [], edges: list[EdgeType] = []):
        self.nodes = nodes  # [A,B,C,D,E]
        self.edges = edges  # [(A,B,x),(A,C,x),(B,E,x),(C,E,x)]

    def __rich__(self):
        return Panel(Group("Nodes:", Pretty(self.nodes), "Edges:", Pretty(self.edges)), title="Nodelist + Edgelist Graph")

    def get_nodes(self) -> list:
        return self.nodes

    def add_node(self, node: NodeType) -> None:
        self.nodes.append(node)

    def add_edge(self, node1, node2, weight=0) -> None:
        self.edges.append((node1, node2, weight))

    def remove_node(self, node: NodeType) -> None:
        self.nodes.remove(node)
        # Also remove all the edges referencing this node
        for edge in self.edges.copy():  # Without a copy, removing an edge during the loop will skip the next edge
            if edge[0] == node or edge[1] == node:
                self.edges.remove(edge)

    def remove_edge(self, node1: NodeType, node2: NodeType, weight: WeightType=0) -> None:
        edge = (node1, node2, weight)
        edge_inverted = (node2, node1, weight)
        if edge in self.edges:
            self.edges.remove(edge)
        if not self.directed and edge_inverted in self.edges:
            self.edges.remove(edge_inverted)

    def get_neighbors(self, node: NodeType) -> list[tuple]:
        neighbors = []
        for edge in self.edges:
            if edge[0] == node:
                neighbors.append((edge[1], edge[2]))
            elif edge[1] == node and not self.directed:
                neighbors.append((edge[0], edge[2]))
        return neighbors


class AdjacencyMatrixGraph(BaseGraph):
    "Graph type storing the data as an adjacency matrix"

    # TODO: Implement adjacency matrix graph

    def init(self, nodes: list[NodeType] = [], edges: list[list[WeightType]] = []):
        self.nodes = nodes  # [A,B,C,D]
        self.matrix = edges  # [[None, None, None, None], [...], [...], [...]]


class AdjacencyListGraph(BaseGraph):
    "Graph type storing the data as an adjacency list"

    # TODO: Implement adjacency list graph

    def init(self):
        pass

# Testing & Example


if __name__ == "__main__":
    g = NodeEdgelistGraph(
        directed=False,
        weighted=True,
        nodes=['A', 'B', 'C',
               'D', 'E', 'F',
               'G', 'H', 'I', ],
        edges=[("A", "B", 2), ("A", "D", 1), ("A", "E", 1), ("B", "C", 5), ("B", "E", 1), ("B", "F", 2), ("C", "F", 3), ("D", "E", 5),
               ("D", "G", 4), ("D", "H", 7), ("E", "F", 2), ("E", "H", 1), ("E", "I", 8), ("F", "I", 4), ("G", "H", 5), ("H", "I", 6)]
    )
    rprint(g)
    rprint("Prim started at A:")
    rprint(g.get_prim_edges("A"))
    rprint("Prim started at I:")
    rprint(g.get_prim_edges("I"))
