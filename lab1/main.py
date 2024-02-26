from easyAI import AI_Player, Negamax

from ConnectFour import ProbabilisticConnectFour
from collections import Counter


NUM_OF_GAMES = 100


if __name__ == "__main__":
    ai_algo_1 = Negamax(3)
    ai_algo_2= Negamax(5)
    results = []
    for _ in range(NUM_OF_GAMES):
        game = ProbabilisticConnectFour([AI_Player(ai_algo_1), AI_Player(ai_algo_2)])
        game.play(verbose=False)
        winner = game.opponent_index if game.lose() else 0
        print("Player %d wins." % winner)
        results.append(winner)
    
    counter = Counter(results)
    print(counter)