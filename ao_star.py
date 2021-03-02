from states import GameTree


class AOStarNode:
    def __init__(self, path=None, parents=None, label=None):
        self.path = []
        self.parents = []
        self.successors = []
        self.label = 0  # Solved == 1, Futile == -1, unknown == 0
        self.__solved = False
        self.__futile = False
        self.__f = 0

    def solved(self):
        self.__solved = True

    def futile(self):
        self.__futile = True

    def cost(self, cost):
        self.__f = cost

    def get_cost(self):
        return self.__f


class AOStar:
    def __init__(self, game):
        self.game = game
        self.init = AOStarNode()
        self.best_path = [self.init]
        self.game_state_tree = self.expand_tree()
        # self.print_tree()

    def expand_tree(self):
        return GameTree(self.game).search()

    # Test method
    def print_tree(self):
        for node in self.game_state_tree:
            print("state, cost: ", node.state.open + node.state.closed, node.cost)

    def init_init(self):
        for state in self.game_state_tree:
            if not state.parent:
                self.init.path.append(state)
                print("cost: ", state.cost)
                self.init.cost(state.cost)
                break
        # self.init.get_cost()

    @staticmethod
    def expand_node(old_node):
        path_param = old_node.path
        for successor in old_node.path[len(old_node.path) - 1].successors:
            if successor.label == 'win':
                label = 1
            elif successor.label == 'loss':
                label = -1
            else:
                label = 0
            old_node.label = label
            path_param.append(successor)
            node = AOStarNode(path_param, old_node, label)
            old_node.successors.append(node)

    def update_cost(self, node):
        parent = node.parent
        while parent:
            branch = False

            parent.cost += node.cost + 1

            if len(parent.successors) > 1:
                for i in parent.successors:
                    if i.cost == 0:
                        parent = None
                        branch = True
            if branch is True:
                    continue

            node = parent
            parent = parent.parent

        if node.parent:
            self.update_cost(node.parent)

    def search(self):
        self.init_init()
        node = self.init

        while self.init.label != 1:
            self.expand_node(node)

