from bfs import Traverse_Tree

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
        self.cost = cost

class AOStar:
    def __init__(self, game):
        self.game = game
        self.init = AOStarNode
        self.graph = [self.init]
        self.game_state_tree = self.expand_tree()

    def expand_tree(self):
        states_bfs = Traverse_Tree(self.game)
        return states_bfs.search()
