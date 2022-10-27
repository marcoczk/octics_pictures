import svgwrite
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from octic_config import IMG_DIRECTORY
from octics_squares import OcticSquares


def create_image(name, proc, num):
    drawing = OcticSquares(IMG_DIRECTORY + name + ".svg", num)
    proc(drawing)
    drawing.save()
    svg_file = svg2rlg(IMG_DIRECTORY + name + ".svg")
    renderPDF.drawToFile(svg_file, IMG_DIRECTORY + name + ".pdf")


def l3_0(image):
    image.add_lines(["P1"], "23", [1, 0.5, 3, 0.5])
    image.add_lines(["P2"], "13", [1, 0.5, 3, 0.5])
    image.add_lines(["P3"], "12", [1, 0.5, 3, 0.5])

def l3_1(image):
    image.add_lines(["P1"], "3'", [1, 0.5, 3, 0.5])
    image.add_lines(["P2"], "3'", [1, 0.5, 3, 0.5])
    image.add_lines(["P3"], "3'", [1, 0.5, 3, 0.5])
    image.add_square("P3'")
    image.add_lines(["P3'"], "1", [4, 0.2, 2, 0.2])
    image.add_lines(["P3'"], "2", [4, 0.5, 2, 0.5])
    image.add_lines(["P3'"], "3", [4, 0.8, 2, 0.8])

def l3_2(image):
    image.add_lines(["P3"], "3'", [1, 0.5, 3, 0.5])
    image.add_square("P3'")
    image.add_lines(["P3'"], "3", [4, 0.8, 2, 0.8])


create_image("new l3_0", l3_0, 3)
create_image("new l3_1", l3_1, 3)
create_image("new l3_2", l3_2, 3)