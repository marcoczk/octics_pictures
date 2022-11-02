from octics_squares import OcticSquares
from svg_export_utils import create_image


def l3_0(image: OcticSquares):
    image.add_lines(["P1"], "23", [0.5, 0, 0.5, 1])
    image.add_lines(["P2"], "13", [0.5, 0, 0.5, 1])
    image.add_lines(["P3"], "12", [0.5, 0, 0.5, 1])


def l3_1(image: OcticSquares):
    image.add_lines(["P1"], "3'", [0.5, 0, 0.5, 1])
    image.add_lines(["P2"], "3'", [0.5, 0, 0.5, 1])
    image.add_lines(["P3"], "3'", [0.5, 0, 0.5, 1])
    image.add_square("P3'")
    image.add_lines(["P3'"], "1", [0, 0.2, 1, 0.2])
    image.add_lines(["P3'"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P3'"], "3", [0, 0.8, 1, 0.8])


def l3_2(image: OcticSquares):
    image.add_lines(["P3"], "3'", [0.5, 0, 0.5, 1])
    image.add_square("P3'")
    image.add_lines(["P3'"], "3", [0, 0.8, 1, 0.8])


create_image("new l3_0", l3_0, 3)
create_image("new l3_1", l3_1, 3)
create_image("new l3_2", l3_2, 3)
