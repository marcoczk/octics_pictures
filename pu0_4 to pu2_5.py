from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# x y z (x+y+z) (x+y+w)=0


squares.add_lines("1", "25", [0, 0, 1, 1])
squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("1", "4", [0, 1, 1, 0])

squares.add_lines("2", "15", [0, 0, 1, 1])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "4", [0, 1, 1, 0])

squares.add_lines("3", "2", [0, 0, 1, 1])
squares.add_lines("3", "1", [0, 0.5, 1, 0.5])
squares.add_lines("3", "45", [0, 1, 1, 0])

squares.add_lines("4", "2", [0, 0, 1, 1])
squares.add_lines("4", "1", [0, 0.5, 1, 0.5])
squares.add_lines("4", "35", [0, 1, 1, 0])

squares.add_lines("5", "12", [0, 0, 1, 1])
squares.add_lines("5", "34", [0, 1, 1, 0])

octic_squares2pdf(squares, "new pu0_4 to pu2_5_0")

squares.add_lines("1", "25", [0, 0.3, 1, 0.3])
squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("1", "4", [0, 0.7, 1, 0.7])
squares.add_lines("1", "5'", [0.5, 0, 0.5, 1], printed_label="5")

squares.add_lines("2", "15", [0, 0.3, 1, 0.3])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "4", [0, 0.7, 1, 0.7])
squares.add_lines("2", "5'", [0.5, 0, 0.5, 1], printed_label="5")

squares.add_lines("3", "2", [0, 0.3, 1, 0.3])
squares.add_lines("3", "1", [0, 0.5, 1, 0.5])
squares.add_lines("3", "45", [0, 0.7, 1, 0.7])
squares.add_lines("3", "5'", [0.5, 0, 0.5, 1], printed_label="5")

squares.add_lines("4", "2", [0, 0.3, 1, 0.3])
squares.add_lines("4", "1", [0, 0.5, 1, 0.5])
squares.add_lines("4", "35", [0, 0.7, 1, 0.7])
squares.add_lines("4", "5'", [0.5, 0, 0.5, 1], printed_label="5")

squares.add_lines("5", "12", [0, 0.4, 1, 0.4])
squares.add_lines("5", "34", [0, 0.6, 1, 0.6])
squares.add_lines("5", "5'", [0.5, 0, 0.5, 1], printed_label="5")

squares.add_square("5'")


squares.add_lines("5'", "1", [0.3, 0, 0.1, 1])
squares.add_lines("5'", "2", [0, 1, 1, 0])
squares.add_lines("5'", "3", [0, 0, 1, 1])
squares.add_lines("5'", "4", [0.1, 0, 0.3, 1])
squares.add_lines("5'", "5", [0, 0.5, 1, 0.5])

octic_squares2pdf(squares, "new pu0_4 to pu2_5_1")
