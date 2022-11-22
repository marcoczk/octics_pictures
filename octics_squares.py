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
        style=SQUARE_LABEL_FONT_STYLE))


def get_line_coords(x1, y1, x2, y2):
    start_coords = int(SQUARE_SIZE * x1), int(SQUARE_SIZE * y1)
    end_coords = int(SQUARE_SIZE * x2), int(SQUARE_SIZE * y2)
    offset_vect = 0, 0
    if y1 == 0:
        offset_vect = (0, -LINE_TEXT_OFFSET)
    elif x1 == 0:
        offset_vect = (-LINE_TEXT_OFFSET - LINE_LABEL_FONT_SIZE / 2, 0)
    elif y1 == 1:
        offset_vect = (0, LINE_TEXT_OFFSET + LINE_LABEL_FONT_SIZE / 2)
    elif x1 == 0:
        offset_vect = (-LINE_TEXT_OFFSET - LINE_LABEL_FONT_SIZE / 2, 0)
    text_coords = (start_coords[0] + offset_vect[0], start_coords[1] + offset_vect[1])
    return start_coords, end_coords, text_coords


def draw_line(dwg, pos, txt, line_info, txt_offset, dashed):
    line_poss = get_line_coords(line_info[0], line_info[1], line_info[2], line_info[3])
    txt_offset_x = txt_offset[0]
    txt_offset_y = txt_offset[1]
    if len(line_info) > 4 and line_info[4] == 'd' or dashed is True:
        dwg.add(dwg.line(
            start=(pos[0] + line_poss[0][0], line_poss[0][1] + pos[1]),
            end=(pos[0] + line_poss[1][0], line_poss[1][1] + pos[1]),
            stroke_width=LINE_STROKE,
            stroke="black",
            style='stroke-dasharray : "2"')
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
        insert=(pos[0] + line_poss[2][0] - int(len(txt) * LINE_LABEL_FONT_SIZE / 4) + txt_offset_x,
                pos[1] + line_poss[2][1] + txt_offset_y),
        style=LINE_LABEL_FONT_STYLE))


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
        style=LINE_LABEL_FONT_STYLE))


class OcticSquares:
    def __init__(self, num_of_squares, _IMG_SIZE=IMG_SIZE):
        self.IMG_SIZE = _IMG_SIZE
        self.num_of_squares = num_of_squares
        self.squares = {}
        self.lines = {}
        self.curr_pos = (LEFT_OFFSET, TOP_OFFSET)
        for i in range(1, num_of_squares + 1):
            label = str(i)
            self.squares[label] = {"label": label, "pos": self.curr_pos}
            self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET, self.curr_pos[1])

    def add_square(self, label):
        self.squares[label] = {"label": label, "pos": self.curr_pos}
        self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET, self.curr_pos[1])

    def add_lines(self, square, label, line_info, printed_label=None, squares=None, txt_offset=(0,0), dashed=False):
        if printed_label is None: printed_label = label
        if squares is None: squares = [square]
        for _square in squares:
            self.lines[_square + ":" + label] = \
                {"label": printed_label, "square": _square, "line_info": line_info,
                 "txt_offset": txt_offset, "dashed": dashed}

    def remove_square(self, label):
        for square_l in self.squares:
            square = self.squares[square_l]
            if square["pos"][0] > self.squares[label]["pos"][0]:
                square["pos"] = (square["pos"][0] - SQUARE_OFFSET - SQUARE_SIZE, square["pos"][1])
        self.curr_pos = (self.curr_pos[0] - SQUARE_OFFSET - SQUARE_SIZE, self.curr_pos[1])
        del self.squares[label]

    def remove_line(self, label):
        del self.lines[label]

    # def add_circles(self, squares, label, center, size):
    #     for square in squares:
    #         draw_circle(self.dwg, self.squares[square], label, center, size)

    def render(self, filename):
        dwg = svgwrite.Drawing(filename=filename, size=self.IMG_SIZE)
        for square_label in self.squares:
            square = self.squares[square_label]
            draw_square(dwg, square["pos"], square["label"])
        for line_label in self.lines:
            line = self.lines[line_label]
            if line["square"] not in self.squares.keys():
                continue
            draw_line(dwg, self.squares[line["square"]]["pos"], line["label"]
                      , line["line_info"], line["txt_offset"], line["dashed"])
        dwg.save()
