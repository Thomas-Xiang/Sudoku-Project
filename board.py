from cell import *
from sudoku_generator import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        if self.difficulty == "easy":
            self.removed_cells = 30
        if self.difficulty == "medium":
            self.removed_cells = 40
        if self.difficulty == "hard":
            self.removed_cells = 50

        self.board = generate_sudoku(BOARD_ROWS, self.removed_cells)
        self.boolean_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.boolean_board[j][i] = True
                else:
                    self.boolean_board[j][i] = False


        self.original_board = self.board[:][:]
        self.sketch_board = [[0 for _ in range(9)] for _ in range(9)]


        self.cell_list = [[], [], [], [], [], [], [], [], []]
        self.sketch_cell_list = [[], [], [], [], [], [], [], [], []]
        self.current_selected = None

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.

        # draw bg color
        pygame.draw.line(self.screen, BG_COLOR, (0, 0), (0, HEIGHT), WIDTH * 2)

        # draw horizontal lines
        for i in range(1, BOARD_ROWS):
            # 3rd parameter: starting point, 4th: ending point
            if i % 3 == 0:
                # bolds every 3rd line
                pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQ_SIZE),
                                 (WIDTH, i * SQ_SIZE), LINE_WIDTH + 3)
            else:
                # normal line
                pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQ_SIZE),
                                 (WIDTH, i * SQ_SIZE), LINE_WIDTH)
        # draw vertical lines
        for i in range(1, BOARD_ROWS):
            if i % 3 == 0:
                # bolds every 3rd line
                pygame.draw.line(self.screen, LINE_COLOR, (i * SQ_SIZE, 0),
                                 (i * SQ_SIZE, HEIGHT), LINE_WIDTH + 3)
            else:
                # normal line
                pygame.draw.line(self.screen, LINE_COLOR, (i * SQ_SIZE, 0),
                                 (i * SQ_SIZE, HEIGHT), LINE_WIDTH)
        # draw cells
        # real cells
        for i in range(9):
            for j in range(9):
                indiv_cell = Cell(value=self.original_board[i][j], row=i, col=j, screen=self.screen, sketch=False)
                indiv_cell.draw(self.screen)

        for i in range(9):
            for j in range(9):
                indiv_cell = Cell(value=self.sketch_board[i][j], row=i, col=j, screen=self.screen, sketch=True)
                indiv_cell.draw(self.screen)

    def select(self, row, column):

        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        self.current_selected = (column, row)
        # 3rd parameter: starting point, 4th: ending point
        # top
        pygame.draw.line(self.screen, SELECT_LINE_COLOR, (SQ_SIZE * row, SQ_SIZE * column),
                         (SQ_SIZE * (row + 1), SQ_SIZE * column), LINE_WIDTH)
        # bottom
        pygame.draw.line(self.screen, SELECT_LINE_COLOR, (SQ_SIZE * row, SQ_SIZE * (column + 1)),
                         (SQ_SIZE * (row + 1), SQ_SIZE * (column + 1)), LINE_WIDTH)
        # left
        pygame.draw.line(self.screen, SELECT_LINE_COLOR, (SQ_SIZE * row, SQ_SIZE * column),
                         (SQ_SIZE * row, SQ_SIZE * (column + 1)), LINE_WIDTH)
        # right
        pygame.draw.line(self.screen, SELECT_LINE_COLOR, (SQ_SIZE * (row + 1), SQ_SIZE * column),
                         (SQ_SIZE * (row + 1), SQ_SIZE * (column + 1)), LINE_WIDTH)

    def click(self, x, y):
        # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the
        # (row, col) of the cell which was clicked. Otherwise, this function returns None.

        # CONCEPT FROM TIC TAC TOE
        # listen for mouse click
        # make sure game isn't over because don't want user to be able to
        # input anything when the game is over
        row = y // SQ_SIZE
        col = x // SQ_SIZE
        if row > 8 or col > 8:
            return None
        else:
            return (row, col)

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves.
        row, col = self.current_selected
        if self.boolean_board[col][row] != True:
            self.board[row][col] = 0
            self.sketch_board[row][col] = 0

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        row = self.current_selected[0]
        column = self.current_selected[1]

        if self.boolean_board[column][row] != True:
            if value == 0:
                self.clear()
        # print(row, column)
            self.board[row][column] = value
            self.sketch_board[row][column] = value

        # print(self.sketch_board)
        # should call draw function in sudoku.py after this function is called to redraw board

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        # checks if the user has selected a cell before assigning
        if self.current_selected is None:
            print("Please select a cell first.")
            return
        # sets actual value of selected cells
        row, col = self.current_selected
        if self.boolean_board[col][row] != True:
            self.board[row][col] = value
            self.sketch_board[row][col] = 0
        # should call draw function in sudoku.py after this function is called to redraw board

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        # resetting to original value
        for i in range(9):
            for j in range(9):
                if self.boolean_board[j][i] == False:
                    self.board[i][j] = 0
                    self.sketch_board[i][j] = 0


    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        # checks to see if board has any zeros left
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        # if all cells have been filled
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.sketch_board[i][j]
                # FIXME - CHECK THIS! should it be sketch_board or something else?

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        # if no empty cells
        return None

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        # checking rows
        win = True

        for row in self.board:
            if set(row) != set(range(1, 10)):
                win = False
        # checking columns
        for j in range(9):
            col = [self.board[i][j] for i in range(9)]
            if set(col) != set(range(1, 10)):
                win = False
        # checks to see if each number appears once in each box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        subgrid.append(self.board[x][y])
                if set(subgrid) != set(range(1, 10)):
                    win = False

        return win
