from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

# x y (x+y+w)

squares = OcticSquares(3)
squares.add_lines("1", "23", [0.5, 0, 0.5, 1])
squares.add_lines("2", "13", [0.5, 0, 0.5, 1])
squares.add_lines("3", "12", [0.5, 0, 0.5, 1])

octic_squares2pdf(squares, "new l3_0")

# STEP 1 - blow up the double line


squares.remove_line("1:23")
squares.remove_line("2:13")
squares.remove_line("3:12")

squares.add_square("3'")
squares.add_lines("1", "3'", [0.5, 0, 0.5, 1])
squares.add_lines("2", "3'", [0.5, 0, 0.5, 1])
squares.add_lines("3", "3'", [0.5, 0, 0.5, 1])
squares.add_lines("3'", "1", [0, 0.2, 1, 0.2])
squares.add_lines("3'", "2", [0, 0.5, 1, 0.5])
squares.add_lines("3'", "3", [0, 0.8, 1, 0.8])

octic_squares2pdf(squares, "new l3_1")

# STEP 2 - blow remaining double lines

squares.remove_line("1:3'")
squares.remove_line("2:3'")
squares.remove_line("3':1")
squares.remove_line("3':2")

octic_squares2pdf(squares, "new l3_2")
