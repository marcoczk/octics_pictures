import svgwrite
from octic_config import *


def draw_square(dwg, pos, txt):
    dwg.add(dwg.rect(
        insert=pos,
        size=(SQUARE_SIZE, SQUARE_SIZE),
        stroke="black",
        stroke_width=SQUARE_STROKE,
        fill="white"))
    dwg.add(dwg.text(
        txt,
        insert=(
            pos[0] + SQUARE_SIZE / 2 - 5,
            pos[1] + SQUARE_SIZE + SQ_TEXT_OFFSET),
        style=FONT_STYLE))


def get_line_coords(x1, y1, x2, y2):
    start_coords = int(SQUARE_SIZE * x1), int(SQUARE_SIZE * y1)
    end_coords = int(SQUARE_SIZE * x2), int(SQUARE_SIZE * y2)
    offset_vect = 0, 0
    if y1 == 0:
        offset_vect = (0, -LINE_TEXT_OFFSET)
    elif x1 == 0:
        offset_vect = (-LINE_TEXT_OFFSET - FONT_SIZE / 2, 0)
    elif y1 == 1:
        offset_vect = (0, LINE_TEXT_OFFSET + FONT_SIZE / 2)
    elif x1 == 0:
        offset_vect = (-LINE_TEXT_OFFSET - FONT_SIZE / 2, 0)
    text_coords = (start_coords[0] + offset_vect[0], start_coords[1] + offset_vect[1])
    return start_coords, end_coords, text_coords


def draw_line(dwg, pos, txt, line_info):
    line_poss = get_line_coords(line_info[0], line_info[1], line_info[2], line_info[3])
    if len(line_info) > 4 and line_info[4] == 'd':
        dwg.add(dwg.line(
            start=(pos[0] + line_poss[0][0], line_poss[0][1] + pos[1]),
            end=(pos[0] + line_poss[1][0], line_poss[1][1] + pos[1]),
            stroke_width=LINE_STROKE,
            stroke="black",
            style='stroke-dasharray:"3"')
        )
    else:
        dwg.add(dwg.line(
            start=(pos[0] + line_poss[0][0], line_poss[0][1] + pos[1]),
            end=(pos[0] + line_poss[1][0], line_poss[1][1] + pos[1]),
            stroke_width=LINE_STROKE,
            stroke="black")
        )
    dwg.add(dwg.text(
        txt,
        insert=(pos[0] + line_poss[2][0] - int(len(txt) * FONT_SIZE / 4), pos[1] + line_poss[2][1]),
        style=FONT_STYLE))


def draw_circle(dwg, pos, txt, center, size):
    circle_center = (int(center[0] + pos[0]), int(center[1] + pos[1]))
    print(circle_center)
    dwg.add(dwg.circle(
        center=circle_center,
        r=CIRCLE_RADIUS * size,
        stroke_width=CIRCLE_STROKE,
        stroke="black",
        fill="white")
    )
    dwg.add(dwg.text(
        txt,
        insert=circle_center,
        style=FONT_STYLE))


class OcticSquares:
    def __init__(self, filename, num_of_squares):
        self.num_of_squares = num_of_squares
        self.dwg = svgwrite.Drawing(filename=filename, size=IMG_SIZE)

        self.squares = {}
        self.curr_pos = (LEFT_OFFSET, TOP_OFFSET)
        for i in range(1, num_of_squares + 1):
            sq_id = "P" + str(i)
            draw_square(self.dwg, self.curr_pos, sq_id)
            self.squares[sq_id] = self.curr_pos
            self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET, self.curr_pos[1])

    def add_square(self, label):
        draw_square(self.dwg, self.curr_pos, label)
        self.squares[label] = self.curr_pos
        self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET, self.curr_pos[1])

    def add_lines(self, squares, label, line_info):
        for square in squares:
            draw_line(self.dwg, self.squares[square], label, line_info)

    def add_circles(self, squares, label, center, size):
        for square in squares:
            draw_circle(self.dwg, self.squares[square], label, center, size)

    def save(self):
        self.dwg.save()
