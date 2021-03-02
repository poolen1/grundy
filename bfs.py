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

class TraverseTree:
    def __init__(self, start_state):
        self.start_node = TreeNode(start_state)
        self.open_nodes = deque()
        self.open_nodes.appendleft(self.start_node)
        self.closed_nodes = deque()

    def search(self):
        while self.open_nodes:
            n = self.open_nodes.pop()
            self.closed_nodes.appendleft(n)

            # print("state: ", n.state.open + n.state.closed)
            # print("open nodes: ", self.open_nodes)

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

        return self.closed_nodes
