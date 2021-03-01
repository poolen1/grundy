

class Grundy:
    def __init__(self, start_stack):
        self.start_stack = start_stack
        self.open = [].append(start_stack)
        self.closed = []
        self.turn = 1  # 1 == + and -1 == -

    # Game move: split chosen stack into two parts
    def split(self, stack, split_0, split_1):

        if split_0 % 2 == 0 and split_1 % 2 == 0:
            print("Can't split into two even stacks")
            return

        index = self.open.index(stack)
        stack = self.open(index)

        self.open.remove(stack)

        if split_0 == 1 or split_0 == 2:
            self.closed.append(split_0)
        else:
            self.open.append(split_0)
        if split_1 == 1 or split_1 == 2:
            self.closed.append(split_1)
        else:
            self.open.append(split_1)

        self.turn *= -1

    def is_game_over(self):
        if self.open:
            return True
        else:
            return False

    def is_win(self):
        if self.turn == -1:
            return True
        else:
            return False

