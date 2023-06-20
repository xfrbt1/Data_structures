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
            [0 for i in range(len(self.VE_DICT))]
            for j in range(len(self.VE_DICT))
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

    def w_adj_matrix(self):
        matrix = [
            [0 for i in range(len(self.VE_DICT))]
            for j in range(len(self.VE_DICT))
        ]

        index_i = 0
        for i in self.VE_DICT:
            index_j = 0
            for j in self.VE_DICT:
                matrix[index_i][index_j] = self.check_adj(i, j)
                index_j += 1
            index_i += 1

        return matrix

    def ind_set(self):
        adj_matrix = self.adj_matrix()

        ind_list = [
            [n for n in self.VE_DICT]
            for i in range(len(self.VE_DICT))
        ]

        # for i in range(len(ind_list)):
        #     for j in range(len(ind_list)):
        #         print(f'{ind_list[i][j]} {adj_matrix[i][j]} |', end=' ')
        #     print(f"->{i}\n")

        for i in range(len(ind_list)):
            for j in range(len(ind_list)):
                if adj_matrix[i][j] != 0:
                    ind_list[i][j] = 'x'

        for i in ind_list:
            print(i)

    def max_ind_set(self):
        pass

    def print_all_nodes(self):
        for k, v in self.VE_DICT.items():
            print(f"{k} -> {v}")


