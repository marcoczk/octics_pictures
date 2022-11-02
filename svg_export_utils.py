from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from octic_config import IMG_DIRECTORY
import os


def octic_squares2pdf(octic_squares, name):
    svg_filename = IMG_DIRECTORY + name + ".svg"
    pdf_filename = IMG_DIRECTORY + name + ".pdf"
    octic_squares.render(svg_filename)
    svg_file = svg2rlg(svg_filename)
    renderPDF.drawToFile(svg_file, pdf_filename)
    os.remove(svg_filename)
