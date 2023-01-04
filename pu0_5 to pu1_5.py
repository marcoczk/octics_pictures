from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# xyz(x+y+wz)(x+2y+z)=0

squares.add_lines("1", "24", [0, 0.5, 1, 0.5])
squares.add_lines("1", "3", [0, 0, 1, 1])
squares.add_lines("1", "5", [0, 1, 1, 0])

squares.add_lines("2", "14", [0, 0.5, 1, 0.5])
squares.add_lines("2", "3", [0, 0, 1, 1])
squares.add_lines("2", "5", [0, 1, 1, 0])

squares.add_lines("3", "1", [0.5, 0, 0.5, 1])
squares.add_lines("3", "2", [0, 0.5, 1, 0.5])
squares.add_lines("3", "4", [0, 1, 1, 0])
squares.add_lines("3", "5", [0, 0, 1, 1])

squares.add_lines("4", "12", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 0, 1, 1])
squares.add_lines("4", "5", [0, 1, 1, 0])

squares.add_lines("5", "1", [0.5, 0, 0.5, 1])
squares.add_lines("5", "2", [0, 0.5, 1, 0.5])
squares.add_lines("5", "3", [0, 1, 1, 0])
squares.add_lines("5", "5", [0, 0, 1, 1])

octic_squares2pdf(squares, "pu0_5 to pu1_5_0")
