import pygame
import sys
from board import *
from constant_variables import *
from sudoku_generator import *


def draw_button(text, center_pos, font, bg_color, text_color):
    text_surface = font.render(text, 0, text_color)
    button_surface = pygame.Surface(
        (text_surface.get_size()[0] + 20, text_surface.get_size()[1] + 20))
    button_surface.fill(bg_color)
    button_surface.blit(text_surface, (10, 10))
    button_rect = button_surface.get_rect(center=center_pos)
    return text_surface, button_surface, button_rect


def draw_game_menu(screen):
    pygame.font.init()
    screen.fill(BG_COLOR)

    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)

    screen.blit(title_font.render("Sudoku", 0, LINE_COLOR),
                title_font.render("Sudoku", 0, LINE_COLOR).get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150)))

    screen.blit(button_font.render("Select Game Mode:", 0, LINE_COLOR),
                button_font.render("Select Game Mode:", 0, LINE_COLOR).get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))

    difficulties = ["Easy", "Medium", "Hard"]
    positions = [(WIDTH - 900 // 2, HEIGHT // 2 + 150),
                 (WIDTH // 2, HEIGHT // 2 + 150),
                 (WIDTH - 300 // 2, HEIGHT // 2 + 150)]
    buttons = {}

    for diff, pos in zip(difficulties, positions):
        text, surface, rect = draw_button(diff, pos, button_font, LINE_COLOR, BG_COLOR)
        screen.blit(surface, rect)
        buttons[diff.lower()] = (text, surface, rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for diff in buttons:
                    if buttons[diff][2].collidepoint(event.pos):
                        return Board(WIDTH, HEIGHT, screen, diff)
            elif event.type == pygame.MOUSEMOTION:
                for diff in buttons:
                    text, surface, rect = buttons[diff]
                    color = BUTTON_DOWN_COLOR if rect.collidepoint(event.pos) else LINE_COLOR
                    surface.fill(color)
                    surface.blit(text, (10, 10))
                    screen.blit(surface, rect)
        pygame.display.update()


def draw_game_buttons(screen):
    pygame.draw.rect(screen, BG_COLOR, pygame.Rect(0, 594, 594, 66))
    button_font = pygame.font.Font(None, 50)

    labels = ["Reset", "Restart", "Exit"]
    positions = [(WIDTH - 900 // 2, HEIGHT - 30),
                 (WIDTH // 2, HEIGHT - 30),
                 (WIDTH - 300 // 2, HEIGHT - 30)]

    buttons = []
    for label, pos in zip(labels, positions):
        text, surface, rect = draw_button(label, pos, button_font, LINE_COLOR, BG_COLOR)
        screen.blit(surface, rect)
        buttons.append((rect, text, surface))

    return buttons


def draw_end_screen(screen, message, button_label):
    screen.fill(BG_COLOR)

    font_main = pygame.font.Font(None, 100)
    font_button = pygame.font.Font(None, 70)

    surface = font_main.render(message, 0, LINE_COLOR)
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(surface, rect)

    text, button, button_rect = draw_button(button_label, (WIDTH // 2, HEIGHT // 2 + 100), font_button, LINE_COLOR, BG_COLOR)
    screen.blit(button, button_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return draw_game_menu(screen) if button_label == "Restart" else sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                color = BUTTON_DOWN_COLOR if button_rect.collidepoint(event.pos) else LINE_COLOR
                button.fill(color)
                button.blit(text, (10, 10))
                screen.blit(button, button_rect)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    board = draw_game_menu(screen)
    screen.fill(BG_COLOR)
    board.draw()
    selected_cell = None
    current_value = None

    while True:
        if board.is_full():
            if board.check_board():
                draw_end_screen(screen, "Game Won! :)", "Exit")
            else:
                board = draw_end_screen(screen, "Game Over :(", "Restart")
                screen.fill(BG_COLOR)
                board.draw()

        for event in pygame.event.get():
            buttons = draw_game_buttons(screen)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, text, _ in buttons:
                    if rect.collidepoint(event.pos):
                        if text.get_text() == "Reset":
                            board.reset_to_original()
                        elif text.get_text() == "Restart":
                            board = draw_game_menu(screen)
                        elif text.get_text() == "Exit":
                            pygame.quit()
                            sys.exit()
                        screen.fill(BG_COLOR)
                        board.draw()
                        break
                else:
                    x, y = event.pos
                    click = board.click(x, y)
                    if click:
                        selected_cell = [click[0], click[1]]
                        board.select(click[1], click[0])
            elif event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:
                    num = event.key - pygame.K_0
                    if num == 0:
                        board.clear()
                    else:
                        current_value = num
                        board.sketch(num)
                elif event.key == pygame.K_RETURN and current_value:
                    board.place_number(current_value)
                elif selected_cell:
                    r, c = selected_cell
                    if event.key == pygame.K_UP and r > 0:
                        selected_cell[0] -= 1
                    elif event.key == pygame.K_DOWN and r < 8:
                        selected_cell[0] += 1
                    elif event.key == pygame.K_LEFT and c > 0:
                        selected_cell[1] -= 1
                    elif event.key == pygame.K_RIGHT and c < 8:
                        selected_cell[1] += 1
                    board.select(selected_cell[1], selected_cell[0])
                board.draw()

        pygame.display.update()
