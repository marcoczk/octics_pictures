from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(4)

# xy(x+y+w)z=0

squares.add_lines("1", "4", [0.5, 0, 0.5, 1])
squares.add_lines("1", "23", [0, 0.5, 1, 0.5])

squares.add_lines("2", "4", [0.5, 0, 0.5, 1])
squares.add_lines("2", "13", [0, 0.5, 1, 0.5])

squares.add_lines("3", "4", [0.5, 0, 0.5, 1])
squares.add_lines("3", "12", [0, 0.5, 1, 0.5])

squares.add_lines("4", "1", [0, 0, 1, 1])
squares.add_lines("4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 1, 1, 0])

octic_squares2pdf(squares, "new pu1_4_0")

# STEP 1 - blowing up L_{12}

squares.add_square("3'")

squares.remove_line("1:23")
squares.remove_line("2:13")
squares.remove_line("3:12")

squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("3", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3'", [0.5, 0, 0.5, 1], dashed=True, printed_label="3")

squares.add_lines("4", "1", [0, 0.2, 1, 0.2])
squares.add_lines("4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 0.8, 1, 0.8])

squares.add_lines("3'", "1", [0, 0.3, 1, 0.3])
squares.add_lines("3'", "2", [0, 0.5, 1, 0.5])
squares.add_lines("3'", "3", [0, 0.7, 1, 0.7])
squares.add_lines("3'", "4", [0.5, 0, 0.5, 1])

# squares.add_lines("3'", "3")

octic_squares2pdf(squares, "new pu1_4_1")

squares.remove_line("1:3")
squares.remove_line("2:3")
squares.remove_line("3':1")
squares.remove_line("3':2")

squares.add_lines("4", "4a", [0.35, 0.15, 0.6, 0.4], dashed=True, printed_label="")
squares.mark_no_intersection("4", "1", "3'")

squares.add_lines("4", "4b", [0.35, 0.45, 0.6, 0.7], dashed=True, printed_label="")
squares.mark_no_intersection("4", "2", "3'")
octic_squares2pdf(squares, "new pu1_4_2")

squares.remove_line("4:1")
squares.remove_line("4:2")
squares.remove_line("1:4")
squares.remove_line("2:4")
octic_squares2pdf(squares, "new pu1_4_3")
