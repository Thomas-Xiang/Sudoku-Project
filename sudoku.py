from sudoku_generator import SudokuGenerator


if __name__ == '__main__':
    sg = SudokuGenerator(9, 30)
    sg.fill_diagonal()
    sg.fill_remaining(0, 3)
    sg.fill_remaining(0, 6)
    sg.fill_remaining(3, 0)
    sg.fill_remaining(3, 6)
    sg.fill_remaining(6, 0)
    sg.fill_remaining(6, 3)
    sg.print_board()