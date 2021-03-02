from grundy import Grundy
from ao_star import AOStar


game = Grundy(6)
strategy = AOStar(game)
strategy.expand_tree()
strategy.calculate_costs()
strategy.print_tree()