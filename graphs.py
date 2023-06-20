class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.VE_DICT = dict()

        for node in self.nodes:
            self.VE_DICT[node] = list()

    def new_node(self, node_name):
        if node_name not in self.VE_DICT:
            self.VE_DICT[node_name] = list()

    def create_links(self, link_list):
        for i in link_list:
            if i[0] in self.VE_DICT:
                self.VE_DICT[i[0]].append([i[1], i[2]])
                self.VE_DICT[i[1]].append([i[0], i[2]])

    def check_adj(self, node1, node2):
        for i in self.VE_DICT[node1]:
            if i[0] == node2:
                return i[1]
        else:
            return 0

    def adj_matrix(self):
        matrix = [
            [0 for i in self.VE_DICT]
            for i in self.VE_DICT
        ]

        index_i = 0
        for i in self.VE_DICT:
            index_j = 0
            for j in self.VE_DICT:
                if self.check_adj(i, j):
                    matrix[index_i][index_j] = 1
                index_j += 1
            index_i += 1

        return matrix

    def weight_adj_matrix(self):
        matrix = [
            [0 for i in self.VE_DICT]
            for i in self.VE_DICT
        ]

        index_i = 0
        for i in self.VE_DICT:
            index_j = 0
            for j in self.VE_DICT:
                matrix[index_i][index_j] = self.check_adj(i, j)
                index_j += 1
            index_i += 1

        return matrix

    def print_wam(self):
        for i in self.weight_adj_matrix():
            print(i)

    def print_am(self):
        for i in self.adj_matrix():
            print(i)

    def nodes_list(self):
        nodes_list = [i for i in self.VE_DICT]
        return nodes_list

    def ind_set(self):
        pass

    def max_ind_set(self):
        pass

    def print_all_nodes(self):
        for k, v in self.VE_DICT.items():
            print(f"{k} -> {v}")


