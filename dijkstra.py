import sys


class node:
    def __init__(self, name, distance=sys.maxsize, start=False, end=False):
        self.name = name
        self.distance = distance
        self.start = start
        self.end = end

    def set_start(self):
        self.start = True
        self.distance = 0

    def set_end(self):
        self.end = True


class edge:
    def __init__(self, v1, v2, distance):
        self.vertices = {v1, v2}
        self.distance = distance


class dijkstra:
    def __init__(self, vertices, edges):
        self.unfinished_vertices = vertices
        self.edges = edges
        self.finished_vertices = set()

    def find_shortest_distance_node(self):
        if len(self.unfinished_vertices) > 0:
            return min(self.unfinished_vertices, key=lambda x: x.distance)
        else:
            return None

    def find_corresponding_edge(self, v1, v2):
        for edge in self.edges:
            if v1 in edge.vertices and v2 in edge.vertices:
                return edge
        return None

    def relax(self):
        current = self.find_shortest_distance_node()
        if current is not None:
            print(current.name)
        if current is None:
            return False
        # Uncomment below if only shortest path is needed
        # elif current.end:
        #     self.finished_vertices.add(current)
        #     self.unfinished_vertices.remove(current)
        #     return True
        else:
            for neighbor in self.unfinished_vertices:
                current_edge = self.find_corresponding_edge(current, neighbor)
                if current_edge is not None:
                    neighbor.distance = min(current.distance + current_edge.distance, neighbor.distance)
            self.finished_vertices.add(current)
            self.unfinished_vertices.remove(current)
            self.relax()

    def display(self):
        for node in self.finished_vertices:
            print(node.name, node.distance)

    def find_shortest_path(self):
        self.relax()
        for final_node in self.finished_vertices:
            if final_node.end:
                return final_node.distance
        return -1

if __name__ == '__main__':
    # Sample example:
    # Nodes
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')
    f = node('f')
    g = node('g')
    z = node('z')
    a.set_start()
    z.set_end()
    vertices = {a, b, c, d, e, f, g, z}

    # Edges
    ab = edge(a, b, 2)
    af = edge(a, f, 1)
    bc = edge(b, c, 2)
    bd = edge(b, d, 2)
    be = edge(b, e, 4)
    ce = edge(c, e, 3)
    cz = edge(c, z, 1)
    de = edge(d, e, 4)
    df = edge(d, f, 3)
    eg = edge(e, g, 7)
    fg = edge(f, g, 5)
    gz = edge(g, z, 6)
    edges = {ab, af, bc, bd, be, ce, cz, de, df, eg, fg, gz}

    shortest_path = dijkstra(vertices, edges)
    print("Shortest path from start to end is:", shortest_path.find_shortest_path())
    print("Nodes with distances:")
    shortest_path.display()
