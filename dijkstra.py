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
        self.stack = []

    def find_shortest_distance_node(self):
        if len(self.unfinished_vertices) > 0:
            shortest_distance_node = min(self.unfinished_vertices, key=lambda x: x.distance)
            self.stack.append(shortest_distance_node);
            return shortest_distance_node
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
            pass
            # print(current.name)
        if current is None:
            return False
        # Uncomment below if only shortest path is needed
        # elif current.end:
        #     self.finished_vertices.add(current)
        #     self.unfinished_vertices.remove(current)
        #     return True
        # Uncomment above if only shortest path is needed
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

    def show_a_shortest_path(self):
        stack = self.stack
        if len(stack) == 0:
            print("ERROR: FIND PATH FIRST")
            return False
        else:
            # Find the end
            a_shortest_path = []
            while len(stack) > 0 and not stack[len(stack) - 1].end:
                stack = stack[:-1]
            if len(stack) == 0:
                print("ERROR: NO PATH POSSIBLE")
                return False

            current_node = stack[len(stack) - 1]
            stack = stack[:-1]
            a_shortest_path.append(current_node)
            print("End Node is Node", current_node.name)
            while len(stack) > 0:
                neighbors = []
                for neighbor in self.finished_vertices:
                    current_edge = self.find_corresponding_edge(current_node, neighbor)
                    if current_edge is not None:
                        neighbors.append(neighbor)
                print("Looking at all nodes for neighbors:")
                for index in range(len(stack)):
                    print("Looking at Node ", stack[index].name, "...", sep='')
                    if stack[index] in neighbors:
                        print("It's the closest neighbor to ", current_node.name, "!", sep='')
                        current_node = stack[index]
                        a_shortest_path.append(current_node)
                        stack = stack[:index]
                        break;

                # print("Looking at Node ", stack[len(stack) - 1].name, "...", sep='')
                # if stack[len(stack) - 1] in neighbors:
                #     print("It's a node in the path!")
                #     current_node = stack[len(stack) - 1]
                #     a_shortest_path.append(current_node)
                # else:
                #     pass
                #     print("Not a node in the path!")
                # stack = stack[:-1]
            print("A possible shortest path is:", "->".join([node.name for node in a_shortest_path[::-1]]))


if __name__ == '__main__':
    # # Sample example:
    # # Nodes
    # a = node('a')
    # b = node('b')
    # c = node('c')
    # d = node('d')
    # e = node('e')
    # f = node('f')
    # g = node('g')
    # z = node('z')
    # a.set_start()
    # z.set_end()
    # vertices = {a, b, c, d, e, f, g, z}
    #
    # # Edges
    # ab = edge(a, b, 2)
    # af = edge(a, f, 1)
    # bc = edge(b, c, 2)
    # bd = edge(b, d, 2)
    # be = edge(b, e, 4)
    # ce = edge(c, e, 3)
    # cz = edge(c, z, 1)
    # de = edge(d, e, 4)
    # df = edge(d, f, 3)
    # eg = edge(e, g, 7)
    # fg = edge(f, g, 5)
    # gz = edge(g, z, 6)
    # edges = {ab, af, bc, bd, be, ce, cz, de, df, eg, fg, gz}

    # a = node('a')
    # b = node('b')
    # c = node('c')
    # d = node('d')
    # vertices = {a, b, c, d}
    # a.set_start()
    # d.set_end()
    #
    # ab = edge(a, b, 1)
    # ac = edge(a, c, 3)
    # ad = edge(a, d, 4)
    # bc = edge(b, c, 1)
    # bd = edge(b, d, 3)
    # cd = edge(c, d, 1)
    # edges = {ab, ac, ad, bc, bd, cd}

    # Nodes
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')
    f = node('f')
    g = node('g')
    h = node('h')
    i = node('i')
    j = node('j')
    z = node('z')
    b.set_start()
    j.set_end()
    vertices = {a, b, c, d, e, f, g, h, i, j, z}

    # Edges
    ab = edge(a, b, 3)
    ae = edge(a, e, 5)
    ah = edge(a, h, 4)
    bc = edge(b, c, 2)
    be = edge(b, e, 5)
    bf = edge(b, f, 7)
    cd = edge(c, d, 3)
    cf = edge(c, f, 2)
    cg = edge(c, g, 6)
    dg = edge(d, g, 7)
    dz = edge(d, z, 2)
    ef = edge(e, f, 4)
    eh = edge(e, h, 7)
    fg = edge(f, g, 4)
    fh = edge(f, h, 5)
    fi = edge(f, i, 4)
    fj = edge(f, j, 3)
    gj = edge(g, j, 4)
    gz = edge(g, z, 6)
    hi = edge(h, i, 2)
    ij = edge(i ,j, 6)
    jz = edge(j, z, 5)
    edges = {ab, ae, ah, bc, be, bf, cd, cf, cg, dg, dz, ef, eh, fg, fh, fi, fj, gj, gz, hi, ij, jz}

    shortest_path = dijkstra(vertices, edges)
    print("Shortest path from start to end is:", shortest_path.find_shortest_path())
    print("We looked through nodes in order of:", ", ".join([node.name for node in shortest_path.stack]))
    print()
    shortest_path.show_a_shortest_path()
    # print("Nodes with distances:")
    # shortest_path.display()
