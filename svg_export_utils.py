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
