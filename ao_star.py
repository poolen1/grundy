from bfs import TraverseTree


class AOStarNode:
    def __init__(self, parents=None):
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

class AOStar:
    def __init__(self, game):
        self.game = game
        self.init = AOStarNode
        self.graph = [self.init]
        self.game_state_tree = self.expand_tree()

    def expand_tree(self):
        return TraverseTree(self.game).search()

    # sum cost
    def calculate_costs(self):
        for node in self.game_state_tree:
            if not node.successors:
                parent = node.parent
                while parent:
                    print("node state: ", node.state.open + node.state.closed, node.cost)
                    print("parent: ", parent.state.open + parent.state.closed, parent.cost)
                    parent = parent.parent
                    if len(parent.successors) > 1:
                        for i in parent.successors:
                            if i.cost == 0:
                                parent = None
                    node = parent

    def print_tree(self):
        for node in self.game_state_tree:
            print("state, cost: ", node.state.open + node.state.closed, node.cost)
