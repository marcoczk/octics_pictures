from octics_squares import OcticSquares
from svg_export_utils import create_image


def pu0_4_0(image: OcticSquares):
    image.add_lines(["P1"], "2", [0, 0, 1, 1])
    image.add_lines(["P1"], "3", [0, 0.5, 1, 0.5])
    image.add_lines(["P1"], "4", [0, 1, 1, 0])

    image.add_lines(["P2"], "1", [0, 0, 1, 1])
    image.add_lines(["P2"], "3", [0, 0.5, 1, 0.5])
    image.add_lines(["P2"], "4", [0, 1, 1, 0])

    image.add_lines(["P3"], "1", [0, 0, 1, 1])
    image.add_lines(["P3"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P3"], "4", [0, 1, 1, 0])

    image.add_lines(["P4"], "1", [0, 0, 1, 1])
    image.add_lines(["P4"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P4"], "3", [0, 1, 1, 0])


def pu0_4_1(image: OcticSquares):
    image.add_lines(["P1"], "3", [0, 0.5, 1, 0.5])
    image.add_lines(["P1"], "4", [0, 1, 1, 0])

    image.add_lines(["P2"], "3", [0, 0.5, 1, 0.5])
    image.add_lines(["P2"], "4", [0, 1, 1, 0])

    image.add_lines(["P3"], "1", [0, 0.2, 1, 0.2])
    image.add_lines(["P3"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P3"], "4", [0, 0.8, 1, 0.8])
    image.add_lines(["P3"], "4", [0.5, 0, 0.5, 1, 'd'])

    image.add_lines(["P4"], "1", [0, 0.2, 1, 0.2])
    image.add_lines(["P4"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P4"], "3", [0, 0.8, 1, 0.8])
    image.add_lines(["P4"], "3", [0.5, 0, 0.5, 1, 'd'])


def pu0_4_2(image: OcticSquares):
    image.add_lines(["P1"], "4", [0, 1, 1, 0])

    image.add_lines(["P2"], "3", [0, 0.5, 1, 0.5])
    image.add_lines(["P2"], "4", [0, 1, 1, 0])

    image.add_lines(["P3"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P3"], "4", [0, 0.8, 1, 0.8])
    image.add_lines(["P3"], "4", [0.5, 0, 0.5, 1, 'd'])

    image.add_lines(["P4"], "1", [0, 0.2, 1, 0.2])
    image.add_lines(["P4"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P4"], "3", [0, 0.8, 1, 0.8])
    image.add_lines(["P4"], "3", [0.5, 0, 0.5, 1, 'd'])
    image.add_lines(["P4"], "", [0.4, 0.1, 0.6, 0.3, 'd'])


def pu0_4_2(image: OcticSquares):
    image.add_lines(["P1"], "4", [0, 1, 1, 0])

    image.add_lines(["P2"], "3", [0, 0.5, 1, 0.5])
    image.add_lines(["P2"], "4", [0, 1, 1, 0])

    image.add_lines(["P3"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P3"], "4", [0, 0.8, 1, 0.8])
    image.add_lines(["P3"], "4", [0.5, 0, 0.5, 1, 'd'])

    image.add_lines(["P4"], "1", [0, 0.2, 1, 0.2])
    image.add_lines(["P4"], "2", [0, 0.5, 1, 0.5])
    image.add_lines(["P4"], "3", [0, 0.8, 1, 0.8])
    image.add_lines(["P4"], "3", [0.5, 0, 0.5, 1, 'd'])
    image.add_lines(["P4"], "", [0.4, 0.1, 0.6, 0.3, 'd'])

create_image("new pu0_4_0", pu0_4_0, 4)
create_image("new pu0_4_1", pu0_4_1, 4)
create_image("new pu0_4_2", pu0_4_2, 4)

