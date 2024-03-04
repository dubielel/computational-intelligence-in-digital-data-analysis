from collections import Counter
from typing import Callable, Type
import time
import json

from easyAI import AI_Player, Negamax, TwoPlayerGame
from easyAI.games import ConnectFour

from ConnectFour import ProbabilisticConnectFour



NUM_OF_GAMES = 100


def time_game(
    game_class: Type[TwoPlayerGame], 
    player1: AI_Player, 
    player2: AI_Player, 
    play_func: Callable[[Type[TwoPlayerGame], AI_Player, AI_Player], int]
) -> tuple[int, float]:
    start = time.perf_counter()
    result = play_func(game_class, player1, player2)
    end = time.perf_counter()
    time_elapsed = end - start

    return result, time_elapsed


def play_game(
    game_class: Type[TwoPlayerGame], player1: AI_Player, player2: AI_Player
) -> int:
    game = game_class([player1, player2])
    game.play(verbose=False)
    winner = game.opponent_index if game.lose() else 0
    print("Player %d wins." % winner)

    return winner


def task1(algo, num_of_games: int) -> None:
    games = (ProbabilisticConnectFour, ConnectFour)
    ultimate_results = {ProbabilisticConnectFour.__name__: [], ConnectFour.__name__: []}
    depths = [(3, 5), (6, 3)]

    for game in games:
        for depth in depths:
            ai_algo_1 = algo(depth[0])
            ai_algo_2 = algo(depth[1])
            player1 = AI_Player(ai_algo_1, name=f"first_{algo.__name__}_d{ai_algo_1.depth}")
            player2 = AI_Player(ai_algo_2, name=f"second_{algo.__name__}_d{ai_algo_2.depth}")
            
            results = []
            for _ in range(num_of_games):
                winner = play_game(game, player1, player2)
                results.append(winner)

            counter = Counter(results)
            print(game.__name__)
            ultimate_results[game.__name__].append(
                {
                    f"d{depth[0]}{depth[1]}": {
                        player1.name: player1.avg_of_times(),
                        player2.name: player2.avg_of_times(),
                        "results": counter
                    }
                }
            )

    with open("task1.json", "w") as fp:
        json.dump(ultimate_results, fp, indent=4)


def main():
    ALGO = Negamax
    GAME = ProbabilisticConnectFour

    ai_algo_1 = ALGO(3)
    ai_algo_2 = ALGO(5)
    player1 = AI_Player(ai_algo_1, name=f"first_{ALGO.__name__}_d{ai_algo_1.depth}")
    player2 = AI_Player(ai_algo_2, name=f"second_{ALGO.__name__}_d{ai_algo_2.depth}")
    results = []
    for _ in range(NUM_OF_GAMES):
        winner = play_game(GAME, player1, player2)
        results.append(winner)

    counter = Counter(results)
    print(counter)


if __name__ == "__main__":
    task1(Negamax, 100)