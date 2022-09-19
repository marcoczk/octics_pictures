import svgwrite
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

from octics_squares import OcticSquares

# dwg = svgwrite.Drawing(filename = "l3_1.svg", size = ("400px", "200px"))
# octics_draw_utils.draw_square(dwg,(100,100),"asd")
# octics_draw_utils.line_mv(dwg,(100,100),"2")

image = OcticSquares("l3_1.svg",3)
image.add_lines(["P1","P2","P3"],"2","mv")
image.add_square("E")
# image.add_lines(["P1","P3","E"],"2","mh")
# image.add_lines(["P2","P3"],"E","md")
# image.add_lines(["E"],"1","od")

image.add_lines(["P2","E"],"E","mh")
image.add_lines(["P1","E"],"2","t14_l34")
image.add_lines(["P1","E"],"3","t17_b57")
image.add_lines(["P1","E"],"1","t67_b27")
image.add_lines(["E"],"1","r34_t34")
image.save()

drawing = svg2rlg("l3_1.svg")
renderPDF.drawToFile(drawing, "file.pdf")


