
class AOStarNode:
    def __init__(self, parents=None):
        self.path = []
        self.parents = []
        self.successors = []
        self.label = 0  # Solved == 1, Futile == -1, unknown == 0
        self.__solved = False
        self.__futile = False

        self.f = self.cost()

    def solved(self):
        self.__solved = True

    def futile(self):
        self.__futile = True

    def cost(self):
        cost = 0
        return cost


class AOStar:
    def __init__(self, game):
        self.game = game
        self.init = AOStarNode()
        self.graph = [self.init]
        self.node = []

