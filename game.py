"""井字棋棋盘"""
import copy

class Board(object):
    def __init__(self):
        self.state = [0,0,0,0,0,0,0,0,0]
        self.winner = None

    def change_state(self, move):
        """move: 11"""
        _copy = copy.deepcopy(self.state)
        player, index = int(move[0]), int(move[1])
        _copy[index] = player
        self.state = _copy
        return _copy

    def init_state(self):
        self.state = [0,0,0,0,0,0,0,0,0]

    def print_board(self):
        for i in range(3):
            print(self.state[i*3:i*3+3])

    def get_legal_moves(self):
        moves = []
        for index in range(9):
            if self.state[index] == 0:
                moves.append(index)
        return moves

    def has_a_winner(self):
        # 行连一起
        if len(set(self.state[0:3])) == 1 and self.state[0] != 0:
            self.winner = self.state[0]
            return True, self.winner
        elif len(set(self.state[3:6])) == 1 and self.state[3] != 0:
            self.winner = self.state[3]
            return True, self.winner
        elif len(set(self.state[6:9])) == 1 and self.state[6] != 0:
            self.winner = self.state[6]
            return True, self.winner
        # 列连一起
        elif len(set(self.state[0:9:3])) == 1 and self.state[0] != 0:
            self.winner = self.state[0]
            return True, self.winner
        elif len(set(self.state[1:9:3])) == 1 and self.state[1] != 0:
            self.winner = self.state[1]
            return True, self.winner
        elif len(set(self.state[2:9:3])) == 1 and self.state[2] != 0:
            self.winner = self.state[2]
            return True, self.winner
        # 两个斜对角
        elif len(set(self.state[0:9:4])) == 1 and self.state[0] != 0:
            self.winner = self.state[0]
            return True, self.winner
        elif len(set(self.state[2:7:2])) == 1 and self.state[2] != 0:
            self.winner = self.state[0]
            return True, self.winner
        else:
            return False, -1

    def game_end(self):
        end, winner = self.has_a_winner()
        if end:
            return True, winner
        elif len(self.get_legal_moves()) == 0:
            # 棋盘满了，平局
            return True, -1
        else:
            return False, -1

class Game(object):
    def __init__(self, board):
        self.board = board

    def start_play(self, player1, player2):
        current_player = player1
        while True:
            move = current_player.get_action(self.board)
            if move == 'Error':
                print("获取动作错误，请重新输入")
                continue
            self.board.change_state(move)
            self.board.print_board()
            end, winner = self.board.game_end()
            if end:
                if winner != -1:
                    print("Game end, winner is ", winner)
                else:
                    print("Game end, Tie")
                return winner
            else:
                current_player = player2 if current_player == player1 else player1

class Player(object):
    def __init__(self, id):
        self.id = id

    def get_action(self, board):
        moves = board.get_legal_moves()
        try:
            user_input = int(input("请下棋："))
        except Exception:
            print("错误的输入")
            return 'Error'
        if user_input in moves:
            return f'{self.id}{user_input}'
        else:
            print("错误的输入")
            return 'Error'



if __name__ == '__main__':
    player1, player2, board = Player(1), Player(2), Board()
    game = Game(board)
    game.start_play(player1, player2)
