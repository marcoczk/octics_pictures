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


def get_point_coords(x, y):
    return int(SQUARE_SIZE * x), int(SQUARE_SIZE * y)


def get_line_coords(x1, y1, x2, y2):
    start_coords = get_point_coords(x1, y1)
    end_coords = get_point_coords(x2, y2)
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
            start=(pos[0] + line_poss[0][0], pos[1] + line_poss[0][1]),
            end=(pos[0] + line_poss[1][0], pos[1] + line_poss[1][1]),
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


def draw_circle(dwg, pos, txt, center, radius):
    circle_center = get_point_coords(center[0], center[1])
    dwg.add(dwg.circle(
        center=(pos[0] + circle_center[0], pos[1] + circle_center[1]),
        r=radius,
        stroke_width=CIRCLE_STROKE,
        stroke="black",
        fill="white")
    )
    dwg.add(dwg.text(
        txt,
        insert=circle_center,
        style=LINE_LABEL_FONT_STYLE))


def find_intersection_of_lines(line1_start, line1_end, line2_start, line2_end):
    x11, y11 = line1_start[0], line1_start[1]
    x12, y12 = line1_end[0], line1_end[1]
    x21, y21 = line2_start[0], line2_start[1]
    x22, y22 = line2_end[0], line2_end[1]
    det = float((x11 - x12) * (y21 - y22) - (y11 - y12) * (x21 - x22))
    if det == 0:
        raise ZeroDivisionError("lines are parallel or coincidental")
    x = ((x11 * y12 - y11 * x12) * (x21 - x22) - (x11 - x12) * (x21 * y22 - y21 * x22)) / det
    y = ((x11 * y12 - y11 * x12) * (y21 - y22) - (y11 - y12) * (x21 * y22 - y21 * x22)) / det
    return x, y


class OcticSquares:
    def __init__(self, num_of_squares, _IMG_SIZE=IMG_SIZE, _CIRCLE_RADIUS=CIRCLE_RADIUS):
        self.IMG_SIZE = _IMG_SIZE
        self.CIRCLE_RADIUS = _CIRCLE_RADIUS
        self.num_of_squares = num_of_squares
        self.squares = {}
        self.lines = {}
        self.circles = {}
        self.curr_pos = (LEFT_OFFSET, TOP_OFFSET)
        for i in range(1, num_of_squares + 1):
            label = str(i)
            self.squares[label] = {"label": label, "pos": self.curr_pos}
            self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET, self.curr_pos[1])

    def add_square(self, label):
        self.squares[label] = {"label": label, "pos": self.curr_pos}
        self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET, self.curr_pos[1])

    def add_lines(self, square, label, line_info, printed_label=None, squares=None, txt_offset=(0, 0), dashed=False):
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

    def remove_line(self, line_label):
        circles_to_remove = []
        for circle_l in self.circles:
            circle = self.circles[circle_l]
            if line_label in [circle["line1"], circle["line2"]]:
                circles_to_remove.append(circle_l)

        for circle_l in circles_to_remove:
            del self.circles[circle_l]
        del self.lines[line_label]

    def remove_lines(self, line_labels):
        for label in line_labels:
            self.remove_line(label)

    def mark_no_intersection(self, square_label, line1_label, line2_label):
        circle_label = square_label + ":" + line1_label + ":" + line2_label
        l1_inf = self.lines[square_label + ":" + line1_label]["line_info"]
        l2_inf = self.lines[square_label + ":" + line2_label]["line_info"]
        intersection = find_intersection_of_lines(
            (l1_inf[0], l1_inf[1]), (l1_inf[2], l1_inf[3]),
            (l2_inf[0], l2_inf[1]), (l2_inf[2], l2_inf[3]))
        self.circles[circle_label] = {"label": circle_label, "pos": intersection, "square": square_label,
                                      "line1": square_label+":"+line1_label, "line2": square_label+":"+line2_label}

    def add_circles(self, squares, label, center, size):
        for square in squares:
            draw_circle(self.dwg, self.squares[square], label, center, size)

    def remove_no_intersection_mark(self, circle_label):
        del self.circles[circle_label]

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
        for circle in self.circles:
            circle = self.circles[circle]
            square_l = circle["square"]
            square = self.squares[square_l]
            draw_circle(dwg, square["pos"], "", circle["pos"], self.CIRCLE_RADIUS)
        dwg.save()
