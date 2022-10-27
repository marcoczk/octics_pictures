import svgwrite
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

from octics_squares import OcticSquares
#
#
# image = OcticSquares("l3_1.svg", 3)
#
# image.add_lines(["P1", "P2", "P3"], "1", [1, 0, 2, 0.5])
# image.add_square("E")
# image.add_lines(["E", "P2", "P3"], "4", [4, 0.8, 2, 0.5])
# image.add_lines(["P2", "P3"], "3", [3, 0.6, 1, 0.5])
# image.add_lines(["E", "P1"], "2", [2, 0.2, 1, 0.5])
# image.add_circles(["P1"], "2", (50, 30), 2)
#
# image.save()
# drawing = svg2rlg("l3_1.svg")
# renderPDF.drawToFile(drawing, "as.pdf")