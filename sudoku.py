import pygame
import sys
from board import *
from constant_variables import *
from sudoku_generator import *


def draw_game_menu(screen):
    """Prints menu screen with 3 difficulty choices"""
    # initialize font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    # fill screen with background color
    screen.fill(BG_COLOR)

    # initialize title and subtitle
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    game_mode_surface = button_font.render("Select Game Mode:", 0, LINE_COLOR)
    game_mode_rectangle = game_mode_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_mode_surface, game_mode_rectangle)

    # initialize button text
    easy_text = button_font.render("Easy", 0, BG_COLOR)
    medium_text = button_font.render("Medium", 0, BG_COLOR)
    hard_text = button_font.render("Hard", 0, BG_COLOR)

    easy_surface = pygame.Surface(
        (easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface(
        (medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface(
        (hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # initalize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH - 900 // 2, HEIGHT // 2 + 150))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH - 300 // 2, HEIGHT // 2 + 150))
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # if mouse clicks easy button, load easy game
                    return Board(WIDTH, HEIGHT, screen, "easy")
                elif medium_rectangle.collidepoint(event.pos):
                    # if mouse clicks medium button, load medium game
                    return Board(WIDTH, HEIGHT, screen, "medium")
                elif hard_rectangle.collidepoint(event.pos):
                    # if mouse clicks hard button, load hard game
                    return Board(WIDTH, HEIGHT, screen, "hard")

            # code to make buttons darker if mouse is over them:
            if event.type == pygame.MOUSEMOTION:
                if easy_rectangle.collidepoint(event.pos):
                    easy_surface.fill(BUTTON_DOWN_COLOR)
                    easy_surface.blit(easy_text, (10, 10))
                    screen.blit(easy_surface, easy_rectangle)
                elif medium_rectangle.collidepoint(event.pos):
                    medium_surface.fill(BUTTON_DOWN_COLOR)
                    medium_surface.blit(medium_text, (10, 10))
                    screen.blit(medium_surface, medium_rectangle)
                elif hard_rectangle.collidepoint(event.pos):
                    hard_surface.fill(BUTTON_DOWN_COLOR)
                    hard_surface.blit(hard_text, (10, 10))
                    screen.blit(hard_surface, hard_rectangle)
                else:
                    easy_surface.fill(LINE_COLOR)
                    medium_surface.fill(LINE_COLOR)
                    hard_surface.fill(LINE_COLOR)
                    easy_surface.blit(easy_text, (10, 10))
                    medium_surface.blit(medium_text, (10, 10))
                    hard_surface.blit(hard_text, (10, 10))
                    screen.blit(easy_surface, easy_rectangle)
                    screen.blit(medium_surface, medium_rectangle)
                    screen.blit(hard_surface, hard_rectangle)

        pygame.display.update()


def draw_game_buttons(screen):
    """displays a bar with the buttons at the bottom during gameplay"""

    # draw rectangle at bottom w background color
    pygame.draw.rect(screen, BG_COLOR, pygame.Rect(0, 594, 594, 66))

    # initialize buttons
    button_font = pygame.font.Font(None, 50)

    reset_text = button_font.render("Reset", 0, BG_COLOR)
    restart_text = button_font.render("Restart", 0, BG_COLOR)
    exit_text = button_font.render("Exit", 0, BG_COLOR)

    reset_surface = pygame.Surface(
        (reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface(
        (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface(
        (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH - 900 // 2, HEIGHT - 30))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT - 30))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH - 300 // 2, HEIGHT - 30))
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    return reset_rectangle, reset_text, reset_surface, restart_rectangle, restart_text, restart_surface, exit_rectangle, exit_text, exit_surface


def draw_game_won(screen):
    """Draws game won screen, with exit button"""

    # initialize fonts
    game_won_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # fill screen with background color
    screen.fill(BG_COLOR)

    # initialize / print "Game Over
    game_won_surface = game_won_font.render("Game Won! :)", 0, LINE_COLOR)
    game_over_rectangle = game_won_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(game_won_surface, game_over_rectangle)

    # initialize restart button
    exit_text = button_font.render("Exit", 0, BG_COLOR)
    exit_surface = pygame.Surface(
        (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    # if mouse clicks, restart and go to main menu
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEMOTION:
                if exit_rectangle.collidepoint(event.pos):
                    exit_surface.fill(BUTTON_DOWN_COLOR)
                    exit_surface.blit(exit_text, (10, 10))
                    screen.blit(exit_surface, exit_rectangle)
                else:
                    exit_surface.fill(LINE_COLOR)
                    exit_surface.blit(exit_text, (10, 10))
                    screen.blit(exit_surface, exit_rectangle)

        pygame.display.update()


def draw_game_over(screen):
    """Draws game over screen, with restart button"""

    # initialize fonts
    game_over_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # fill screen with background color
    screen.fill(BG_COLOR)

    # initialize / print "Game Over
    game_over_surface = game_over_font.render("Game Over :(", 0, LINE_COLOR)
    game_over_rectangle = game_over_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(game_over_surface, game_over_rectangle)

    # initialize restart button
    restart_text = button_font.render("Restart", 0, BG_COLOR)
    restart_surface = pygame.Surface(
        (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    # if mouse clicks, restart and go to main menu
                    return draw_game_menu(screen)

            if event.type == pygame.MOUSEMOTION:
                if restart_rectangle.collidepoint(event.pos):
                    restart_surface.fill(BUTTON_DOWN_COLOR)
                    restart_surface.blit(restart_text, (10, 10))
                    screen.blit(restart_surface, restart_rectangle)
                else:
                    restart_surface.fill(LINE_COLOR)
                    restart_surface.blit(restart_text, (10, 10))
                    screen.blit(restart_surface, restart_rectangle)
        pygame.display.update()


if __name__ == "__main__":
    # pygame template

    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # start menu and initalize board
    board = draw_game_menu(screen)

    screen.fill(BG_COLOR)
    board.draw()

    # selected cell for arrow keys
    selected_cell = None

    while True:
        # event handler

        if board.is_full():
            if board.check_board():
                # if game is won
                draw_game_won(screen)
            else:
                # if game is lost
                board = draw_game_over(screen)
                screen.fill(BG_COLOR)
                board.draw()

        for event in pygame.event.get():

            # buttons areas
            reset_rectangle, reset_text, reset_surface, restart_rectangle, restart_text, restart_surface, exit_rectangle, exit_text, exit_surface = draw_game_buttons(
                screen)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # listen for mouse click
                # make sure game isn't over because don't want user to be able to
                # input anything when the game is over
                # and not game_over
                # cell_selected = True
                if reset_rectangle.collidepoint(event.pos):
                    # if mouse clicks, reset board
                    board.reset_to_original()
                    screen.fill(BG_COLOR)
                    board.draw()
                elif restart_rectangle.collidepoint(event.pos):
                    # if mouse clicks, restart and go to main menu
                    board = draw_game_menu(screen)
                    screen.fill(BG_COLOR)
                    board.draw()
                elif exit_rectangle.collidepoint(event.pos):
                    # if mouse clicks, exit game
                    pygame.quit()
                    sys.exit()
                else:
                    # selects a cell
                    board.draw()
                    x, y = event.pos  # unpack x,y coords with tuple
                    click = board.click(x, y)
                    if click is not None:
                        selected_cell = [click[0], click[1]]
                        board.select(click[1], click[0])

            elif event.type == pygame.KEYDOWN:  # and cell_selected == True
                # press 1 key
                if event.key == pygame.K_1:
                    current_value = 1
                    board.sketch(current_value)
                # press 2 key
                if event.key == pygame.K_2:
                    current_value = 2
                    board.sketch(current_value)
                # press 3 key
                if event.key == pygame.K_3:
                    current_value = 3
                    board.sketch(current_value)
                # press 4 key
                if event.key == pygame.K_4:
                    current_value = 4
                    board.sketch(current_value)
                # press 5 key
                if event.key == pygame.K_5:
                    current_value = 5
                    board.sketch(current_value)
                # press 6 key
                if event.key == pygame.K_6:
                    current_value = 6
                    board.sketch(current_value)
                # press 7 key
                if event.key == pygame.K_7:
                    current_value = 7
                    board.sketch(current_value)
                # press 8 key
                if event.key == pygame.K_8:
                    current_value = 8
                    board.sketch(current_value)
                # press 9 key
                if event.key == pygame.K_9:
                    current_value = 9
                    board.sketch(current_value)
                if event.key == pygame.K_0:
                    current_value = 0
                    board.clear()
                # press enter key
                # FIXME reset current_value to none when new cell is selected
                if event.key == pygame.K_RETURN and current_value is not None:
                    board.place_number(current_value)
                board.draw()
                if selected_cell is None:
                    if event.key == pygame.K_UP:
                        board.select(0, 0)
                        board.draw()
                    if event.key == pygame.K_DOWN:
                        board.select(0, 0)
                        board.draw()
                    if event.key == pygame.K_RIGHT:
                        board.select(0, 0)
                        board.draw()
                    if event.key == pygame.K_LEFT:
                        board.select(0, 0)
                        board.draw()
                if selected_cell is not None:
                    if event.key == pygame.K_UP:
                        board.draw()
                        if selected_cell[0] < 9 and selected_cell[0] > -1:
                            selected_cell[0] -= 1
                        board.select(selected_cell[1], selected_cell[0])
                    if event.key == pygame.K_DOWN:
                        board.draw()
                        if selected_cell[0] < 9 and selected_cell[0] > -1:
                            selected_cell[0] += 1
                        board.select(selected_cell[1], selected_cell[0])
                    if event.key == pygame.K_RIGHT:
                        board.draw()
                        if selected_cell[1] < 9 and selected_cell[1] > -1:
                            selected_cell[1] += 1
                        board.select(selected_cell[1], selected_cell[0])
                    if event.key == pygame.K_LEFT:
                        board.draw()
                        if selected_cell[1] < 9 and selected_cell[1] > -1:
                            selected_cell[1] -= 1
                        board.select(selected_cell[1], selected_cell[0])

            elif event.type == pygame.MOUSEMOTION:
                # the code below this is for making buttons darker
                if reset_rectangle.collidepoint(event.pos):
                    reset_surface.fill(BUTTON_DOWN_COLOR)
                    reset_surface.blit(reset_text, (10, 10))
                    screen.blit(reset_surface, reset_rectangle)
                elif restart_rectangle.collidepoint(event.pos):
                    restart_surface.fill(BUTTON_DOWN_COLOR)
                    restart_surface.blit(restart_text, (10, 10))
                    screen.blit(restart_surface, restart_rectangle)
                elif exit_rectangle.collidepoint(event.pos):
                    exit_surface.fill(BUTTON_DOWN_COLOR)
                    exit_surface.blit(exit_text, (10, 10))
                    screen.blit(exit_surface, exit_rectangle)
                else:
                    reset_surface.fill(LINE_COLOR)
                    restart_surface.fill(LINE_COLOR)
                    exit_surface.fill(LINE_COLOR)
                    reset_surface.blit(reset_text, (10, 10))
                    restart_surface.blit(restart_text, (10, 10))
                    exit_surface.blit(exit_text, (10, 10))
                    screen.blit(reset_surface, reset_rectangle)
                    screen.blit(restart_surface, restart_rectangle)
                    screen.blit(exit_surface, exit_rectangle)
        pygame.display.update()