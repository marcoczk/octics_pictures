from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(4)

# xy(x+y+zw)z=0

squares.add_lines("1", "4", [0.5, 0, 0.5, 1])
squares.add_lines("1", "23", [0, 0.5, 1, 0.5])

squares.add_lines("2", "4", [0.5, 0, 0.5, 1])
squares.add_lines("2", "13", [0, 0.5, 1, 0.5])

squares.add_lines("3", "4", [0.5, 0, 0.5, 1])
squares.add_lines("3", "12", [0, 0.5, 1, 0.5])

squares.add_lines("4", "1", [0, 0, 1, 1])
squares.add_lines("4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 1, 1, 0])

octic_squares2pdf(squares, "pu0_4 to pu1_4_0")

# squares.add_lines("", "E", [0.5, 0, 0.5, 1], printed_label="", squares=["1", "2", "3", "4"], dashed=True)

squares.add_lines("1", "4", [0, 0.4, 1, 0.4])
squares.add_lines("1", "23", [0, 0.6, 1, 0.6])

squares.add_lines("2", "4", [0, 0.4, 1, 0.4])
squares.add_lines("2", "13", [0, 0.6, 1, 0.6])

squares.add_lines("3", "4", [0, 0.4, 1, 0.4])
squares.add_lines("3", "12", [0, 0.6, 1, 0.6])

squares.add_lines("4", "1", [0, 0.3, 1, 0.3])
squares.add_lines("4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 0.7, 1, 0.7])

octic_squares2pdf(squares, "pu0_4 to pu1_4_1")
