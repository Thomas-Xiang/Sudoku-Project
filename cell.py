from constant_variables import *
import pygame


class Cell:
    def __init__(self, value, row, col, screen, sketch):
        # Constructor for the Cell class
        self.value = str(value)
        self.row = row
        self.col = col
        self.screen = screen

        # We need to figure out how to make this true when the user selects the cell
        self.selected = False

        # tells whether sketch or not
        self.sketch = sketch

    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = str(value)

    # Not too sure about the difference between these two methods
    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.value = str(value)

    def draw(self, screen):
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
        # draw 'x' or 'o' as text in the window/board

        # 2. text drawing: define the text
        chip_font = pygame.font.Font(None, 50)

        if self.sketch == False:
            # We need to decide on a font color for the numbers (that is the third parameter in chip_font.render())
            one = chip_font.render('1', True, NUMBER_COLOR)
            two = chip_font.render('2', True, NUMBER_COLOR)
            three = chip_font.render('3', True, NUMBER_COLOR)
            four = chip_font.render('4', True, NUMBER_COLOR)
            five = chip_font.render('5', True, NUMBER_COLOR)
            six = chip_font.render('6', True, NUMBER_COLOR)
            seven = chip_font.render('7', True, NUMBER_COLOR)
            eight = chip_font.render('8', True, NUMBER_COLOR)
            nine = chip_font.render('9', True, NUMBER_COLOR)

            # We need to figure out square size
            if self.selected:
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(self.col * SQ_SIZE, self.row *
                                             SQ_SIZE, SQ_SIZE, SQ_SIZE), 12)

            # sets center coords
            num_center = (self.col * SQ_SIZE + SQ_SIZE // 2, self.row *
                          SQ_SIZE + SQ_SIZE // 2)

        if self.sketch == True:
            # We need to decide on a font color for the numbers (that is the third parameter in chip_font.render())
            one = chip_font.render('1', True, SKETCH_NUM_COLOR)
            two = chip_font.render('2', True, SKETCH_NUM_COLOR)
            three = chip_font.render('3', True, SKETCH_NUM_COLOR)
            four = chip_font.render('4', True, SKETCH_NUM_COLOR)
            five = chip_font.render('5', True, SKETCH_NUM_COLOR)
            six = chip_font.render('6', True, SKETCH_NUM_COLOR)
            seven = chip_font.render('7', True, SKETCH_NUM_COLOR)
            eight = chip_font.render('8', True, SKETCH_NUM_COLOR)
            nine = chip_font.render('9', True, SKETCH_NUM_COLOR)

            # We need to figure out square size
            if self.selected:
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(self.col * SQ_SIZE, self.row *
                                             SQ_SIZE, SQ_SIZE, SQ_SIZE), 12)

            # sets center coords
            num_center = (self.col * SQ_SIZE + SQ_SIZE // 4, self.row *
                          SQ_SIZE + SQ_SIZE // 4)

        if self.value == '1':
            # 3. text drawing: define the location
            one_rect = one.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(one, one_rect)

        elif self.value == '2':
            # 3. text drawing: define the location
            two_rect = two.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(two, two_rect)

        elif self.value == '3':
            # 3. text drawing: define the location
            three_rect = three.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(three, three_rect)

        elif self.value == '4':
            # 3. text drawing: define the location
            four_rect = four.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(four, four_rect)

        elif self.value == '5':
            # 3. text drawing: define the location
            five_rect = five.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(five, five_rect)

        elif self.value == '6':
            # 3. text drawing: define the location
            six_rect = six.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(six, six_rect)

        elif self.value == '7':
            # 3. text drawing: define the location
            seven_rect = seven.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(seven, seven_rect)

        elif self.value == '8':
            # 3. text drawing: define the location
            eight_rect = eight.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(eight, eight_rect)

        elif self.value == '9':
            # 3. text drawing: define the location
            nine_rect = nine.get_rect(
                center=num_center)
            # 4. # text drawing: blit the number onto the screen
            screen.blit(nine, nine_rect)