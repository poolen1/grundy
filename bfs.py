from grundy import Grundy
import copy
import queue

class TreeNode:
    def __init__(self, game, parent=None, label=None):
        self.state = game
        self.parent = parent
        self.label = label


class Traverse_Tree:
    def __init__(self, start_state):
        self.start_node = TreeNode(start_state)
        self.open_nodes = queue.Queue()
        self.open_nodes.put(self.start_node)
        self.closed_nodes = queue.Queue()

    def search(self):
        while self.open_nodes:
            n = self.open_nodes.get()
            self.closed_nodes.put(n)

            print("state: ", n.state.open + n.state.closed)

            for stack in n.state.open:
                low_range = int(stack / 2) + 1
                for split_0 in range(low_range, stack):
                    split_1 = stack - split_0
                    new_game = copy.deepcopy(n.state)
                    new_game.split(stack, split_0, split_1)
                    new_node = TreeNode(new_game)
                    self.open_nodes.put(new_node)

