from grundy import Grundy
from ao_star import AOStar


game = Grundy(6)
strategy_engine = AOStar(game)
strategy_engine.search()
# strategy.print_tree()
