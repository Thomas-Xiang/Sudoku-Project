import pygame
import sys
from board import *
from constant_variables import *
from sudoku_generator import *


def draw_button(text, center_pos, font, bg_color, text_color):
    text_surface = font.render(text, True, text_color)
    button_surface = pygame.Surface((text_surface.get_size()[0] + 20, text_surface.get_size()[1] + 20))
    button_surface.fill(bg_color)
    button_surface.blit(text_surface, (10, 10))
    button_rect = button_surface.get_rect(center=center_pos)
    return text, button_surface, button_rect


def draw_game_buttons(screen):
    pygame.draw.rect(screen, BG_COLOR, pygame.Rect(0, 594, 594, 66))
    button_font = pygame.font.Font(None, 40)

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



def draw_game_menu(screen):
    screen.fill(BG_COLOR)
    title_font = pygame.font.SysFont(None, 65)
    mode_font = pygame.font.SysFont(None, 50)
    button_font = pygame.font.SysFont("comicsans", 20)


    title_surface = title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    mode_surface = mode_font.render("Select Game Mode", True, LINE_COLOR)
    mode_rectangle = mode_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mode_surface, mode_rectangle)

    # Draw difficulty buttons
    buttons = []
    difficulties = ["EASY", "MEDIUM", "HARD"]
    positions = [(WIDTH // 2 - 150, HEIGHT // 2 + 150),
                 (WIDTH // 2, HEIGHT // 2 + 150),
                 (WIDTH // 2 + 150, HEIGHT // 2 + 150)]
    for label, pos in zip(difficulties, positions):
        text_surface = button_font.render(label, True, LINE_COLOR)
        button_rect = text_surface.get_rect(center = pos)
        button_surface = pygame.Surface((button_rect.width + 20, button_rect.height + 20))
        button_surface.fill(SELECT_LINE_COLOR)
        button_surface.blit(text_surface, (10, 10))
        screen.blit(button_surface, button_rect)
        buttons.append((button_rect, label))  # Store rect and label

    pygame.display.update()

    # Wait for difficulty selection
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, label in buttons:
                    if rect.collidepoint(event.pos):
                        return Board(WIDTH, HEIGHT, screen, label.lower())  # Create board with selected difficulty




def draw_end_screen(screen, message, button_label):
    font = pygame.font.SysFont(None, 50)
    button_font = pygame.font.SysFont(None, 40)

    # Clear screen and draw message
    screen.fill((255, 255, 255))
    text_surface = font.render(message, True, (0, 0, 0))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 150))

    # Draw button
    button_text = button_font.render(button_label, True, (255, 255, 255))
    button_rect = pygame.Rect(WIDTH // 2 - 75, 300, 150, 50)
    pygame.draw.rect(screen, (0, 0, 0), button_rect)
    screen.blit(button_text, (button_rect.x + (150 - button_text.get_width()) // 2,
                              button_rect.y + (50 - button_text.get_height()) // 2))

    pygame.display.update()

    # Wait for click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    if button_label.lower() == "restart":
                        return Board(WIDTH, HEIGHT, screen, "medium")  # Default difficulty or modify as needed



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
                for rect, label, _ in buttons:
                    if rect.collidepoint(event.pos):
                        if label == "Reset":
                            board.reset_to_original()
                            screen.fill(BG_COLOR)
                            board.draw()
                        elif label == "Restart":
                            board = draw_game_menu(screen)
                            screen.fill(BG_COLOR)
                            board.draw()
                        elif label == "Exit":
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
