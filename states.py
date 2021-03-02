from grundy import Grundy
import copy
from collections import deque
import queue


class TreeNode:
    def __init__(self, game, parent=None):
        self.state = game
        self.parent = parent
        self.successors = []
        self.cost = 0
        self.label = ""

    def update_cost(self, cost):
        self.cost = cost

    def update_label(self, label):
        self.label = label


class GameTree:
    def __init__(self, start_state):
        self.start_node = TreeNode(start_state)
        self.open_nodes = deque()
        self.open_nodes.appendleft(self.start_node)
        self.closed_nodes = deque()

    def search(self):
        while self.open_nodes:
            n = self.open_nodes.pop()
            self.closed_nodes.appendleft(n)

            for stack in n.state.open:
                low_range = int(stack / 2) + 1
                for split_0 in range(low_range, stack):
                    split_1 = stack - split_0

                    new_game = copy.deepcopy(n.state)
                    new_game.split(stack, split_0, split_1)

                    new_node = TreeNode(new_game)
                    new_node.parent = n

                    if new_node.state.is_game_over():
                        new_node.update_cost(0)
                        if new_node.state.is_win():
                            new_node.update_label("win")
                        else:
                            new_node.update_label("loss")

                    n.successors.append(new_node)

                    self.open_nodes.appendleft(new_node)

        closed_nodes = self.calculate_state_costs(list(self.closed_nodes))

        return closed_nodes

    # sum cost
    @staticmethod
    def calculate_state_costs(tree):
        for node in tree:
            if not node.successors:
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

        return tree
