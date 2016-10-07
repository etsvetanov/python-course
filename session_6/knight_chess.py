def field_to_indexes(field):
    """ columns are y (letters), rows are x (numbers)"""

    letter, number = field
    dictionary = {key: value for value, key in list(enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))}
    y = dictionary[letter]
    x = int(number) - 1

    return x, y

class ChessPiece:
    def __init__(self):
        self.position = None
        self.board = None
        self.history = []

    def make_a_move(self, field):
        raise NotImplementedError

    def is_valid_move(self, destination):
        raise NotImplementedError


class Knight(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

        self.valid_moves = [
            (2, 1),
            (1, 2)
        ]

    def is_valid_move(self, destination):
        src_x, src_y = self.position
        correct_moves = []

        for move in self.valid_moves:
            move_x, move_y = move
            correct_moves.append((src_x + move_x, src_y + move_y))
            correct_moves.append((src_x - move_x, src_y - move_y))
            correct_moves.append((src_x + move_x, src_y - move_y))
            correct_moves.append((src_x - move_x, src_y + move_y))

        if destination in correct_moves:
            return True
        else:
            return False

    def make_a_move(self, field):
        x, y = field_to_indexes(field)
        destination = (x, y)

        if self.is_valid_move(destination):
            self.board.move(self, destination)
        else:
            print('Invalid move')


    def __str__(self):
        return 'K'

class Chessboard:
    def __init__(self):
        self.chess_fields = [[None for i in range(8)] for j in range(8)]

    def add_piece(self, piece, field):
        x, y = field_to_indexes(field)
        self.chess_fields[x][y] = piece
        piece.board = self
        piece.position = x, y

    def move(self, piece, destination):
        source = piece.position
        src_x, src_y = source
        dst_x, dst_y = destination

        self.chess_fields[src_x][src_y] = None
        self.chess_fields[dst_x][dst_y] = piece

    def __str__(self):
        row = ''.join('{:5} ' for i in range(9)) + '\n'
        rows = ''.join(row for i in range(9))
        fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        for i in range(8):
            fields.append(i+1)
            fields += [str(field) for field in self.chess_fields[i]]

        return rows.format(*fields)

if __name__ == '__main__':
    board = Chessboard()
    print(board)
    knight = Knight()
    board.add_piece(knight, 'b1')
    print(board)
    knight.make_a_move('a3')
    print(board)

