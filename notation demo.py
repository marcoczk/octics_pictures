from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5)
# x y z (x+2y+z) (x+y)

squares.add_lines("1", "25", [0, 0, 1, 1])
squares.add_lines("1", "3", [0, 1, 1, 0])
squares.add_lines("1", "4", [0, 0.5, 1, 0.5])

squares.add_lines("2", "15", [0, 0, 1, 1])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "4", [0, 1, 1, 0])

squares.add_lines("3", "1", [0, 0, 1, 1])
squares.add_lines("3", "2", [0.5, 0, 0.5, 1])
squares.add_lines("3", "4", [0, 0.5, 1, 0.5])
squares.add_lines("3", "5", [0, 1, 1, 0])

squares.add_lines("4", "1", [0, 0, 1, 1])
squares.add_lines("4", "2", [0.5, 0, 0.5, 1])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "5", [0, 1, 1, 0])

squares.add_lines("5", "12", [0, 0, 1, 1])
squares.add_lines("5", "3", [0, 1, 1, 0])
squares.add_lines("5", "4", [0, 0.5, 1, 0.5])

octic_squares2pdf(squares, "demo_1")

# STEP 1 - blow-up of the fivefold point


squares = OcticSquares(5, _IMG_SIZE=(800, 120))

squares.add_square("A")

squares.add_lines("1", "25", [0, 0.2, 1, 0.2])
squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("1", "4", [0, 0.8, 1, 0.8])

squares.add_lines("2", "15", [0, 0.2, 1, 0.2])
squares.add_lines("2", "4", [0, 0.5, 1, 0.5])
squares.add_lines("2", "5", [0, 0.8, 1, 0.8])

squares.add_lines("3", "1", [0, 0.2, 1, 0.2])
squares.add_lines("3", "2", [0, 0.4, 1, 0.4])
squares.add_lines("3", "4", [0, 0.6, 1, 0.6])
squares.add_lines("3", "5", [0, 0.8, 1, 0.8])

squares.add_lines("4", "1", [0, 0.2, 1, 0.2])
squares.add_lines("4", "2", [0, 0.4, 1, 0.4])
squares.add_lines("4", "3", [0, 0.6, 1, 0.6])
squares.add_lines("4", "5", [0, 0.8, 1, 0.8])

squares.add_lines("5", "12", [0, 0.2, 1, 0.2])
squares.add_lines("5", "3", [0, 0.5, 1, 0.5])
squares.add_lines("5", "4", [0, 0.8, 1, 0.8])

squares.add_lines("", "A", [0.5, 0, 0.5, 1, 'd'], squares=["1", "2", "3", "4", "5"])

squares.add_lines("A", "1", [0, 0.5, 1, 0.5])
squares.add_lines("A", "2", [0, 1, 1, 0])
squares.add_lines("A", "5", [0, 0, 1, 1])
squares.add_lines("A", "3", [0.6, 0, 0.2, 1])
squares.add_lines("A", "4", [0.4, 0, 0.8, 1])

octic_squares2pdf(squares, "demo_2")

