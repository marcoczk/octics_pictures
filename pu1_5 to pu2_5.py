from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5)
# x y (x+y) z (x+wy+z)
squares.add_lines("1", "23", [0, 0, 1, 1])
squares.add_lines("1", "45", [0, 1, 1, 0])

squares.add_lines("2", "13", [0, 0, 1, 1])
squares.add_lines("2", "4", [0, 0.5, 1, 0.5])
squares.add_lines("2", "5", [0, 1, 1, 0])

squares.add_lines("3", "12", [0, 0, 1, 1])
squares.add_lines("3", "4", [0, 0.5, 1, 0.5])
squares.add_lines("3", "5", [0, 1, 1, 0])

squares.add_lines("4", "2", [0, 0, 1, 1])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "15", [0, 1, 1, 0])

squares.add_lines("5", "2", [0, 0, 1, 1])
squares.add_lines("5", "3", [0, 0.5, 1, 0.5])
squares.add_lines("5", "14", [0, 1, 1, 0])

octic_squares2pdf(squares, "new pu1_5 to pu2_5_0")
# STEP 1 - blow up the fivefold point

squares = OcticSquares(5, _IMG_SIZE=(800, 120))

squares.add_square("A")

squares.add_lines("1", "23", [0, 0.2, 1, 0.2])
squares.add_lines("1", "45", [0, 0.8, 1, 0.8])

squares.add_lines("2", "13", [0, 0.2, 1, 0.2])
squares.add_lines("2", "4", [0, 0.5, 1, 0.5])
squares.add_lines("2", "5", [0, 0.8, 1, 0.8])

squares.add_lines("3", "12", [0, 0.2, 1, 0.2])
squares.add_lines("3", "4", [0, 0.5, 1, 0.5])
squares.add_lines("3", "5", [0, 0.8, 1, 0.8])

squares.add_lines("4", "2", [0, 0.2, 1, 0.2])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "15", [0, 0.8, 1, 0.8])

squares.add_lines("5", "2", [0, 0.2, 1, 0.2])
squares.add_lines("5", "3", [0, 0.5, 1, 0.5])
squares.add_lines("5", "14", [0, 0.8, 1, 0.8])

squares.add_lines("", "A", [0.5, 0, 0.5, 1, 'd'], squares=["1", "2", "3", "4", "5"])

squares.add_lines("A", "1", [0, 0.5, 1, 0.5])
squares.add_lines("A", "2", [0, 1, 1, 0])
squares.add_lines("A", "3", [0, 0, 1, 1])
squares.add_lines("A", "4", [0.1, 0, 0.3, 1])
squares.add_lines("A", "5", [0.3, 0, 0.1, 1])

octic_squares2pdf(squares, "new pu1_5 to pu2_5_1")

# STEP 2 - blow-up of the line L_{123}

squares.add_square("B")

squares.remove_line("1:23")
squares.remove_line("2:13")
squares.remove_line("3:12")
squares.add_lines("", "B", [0, 0.2, 1, 0.2], squares=["1", "2", "3"])

squares.add_lines("A", "B", [0.5, 0, 0.5, 1, 'd'])
squares.add_lines("A", "3", [0, 0.2, 1, 0.2])
squares.add_lines("A", "1", [0, 0.5, 1, 0.5])
squares.add_lines("A", "2", [0, 0.8, 1, 0.8])

squares.add_lines("B", "1", [0, 0.2, 1, 0.2])
squares.add_lines("B", "2", [0, 0.5, 1, 0.5])
squares.add_lines("B", "3", [0, 0.8, 1, 0.8])
squares.add_lines("B", "A", [0.5, 0, 0.5, 1])

octic_squares2pdf(squares, "new pu1_5 to pu2_5_2")

# STEP 3 - blow-up of the lines L_{1B}, L_{2B}, L_{3B}$, L_{24}$, L_{25}, L_{34}, L_{35}

squares.remove_line("1:B")
squares.remove_line("2:B")
squares.remove_line("2:4")
squares.remove_line("2:5")
squares.remove_line("3:B")
squares.remove_line("3:4")
squares.remove_line("3:5")
squares.remove_line("4:2")
squares.remove_line("4:3")
squares.remove_line("5:2")
squares.remove_line("5:3")
squares.remove_line("B:1")
squares.remove_line("B:2")
squares.remove_line("B:3")

squares.add_lines("A", "Aa", [0.44, 0.1, 0.56, 0.3, 'd'], printed_label="")
squares.add_lines("A", "Ab", [0.44, 0.4, 0.56, 0.6, 'd'], printed_label="")
squares.add_lines("A", "Ac", [0.44, 0.7, 0.56, 0.9, 'd'], printed_label="")

squares.add_lines("A", "Ad", [0.08, 0.1, 0.2, 0.3, 'd'], printed_label="")
squares.add_lines("A", "Ae", [0.2, 0.1, 0.32, 0.3, 'd'], printed_label="")
squares.add_lines("A", "Af", [0.08, 0.7, 0.2, 0.9, 'd'], printed_label="")
squares.add_lines("A", "Ag", [0.2, 0.7, 0.32, 0.9, 'd'], printed_label="")

octic_squares2pdf(squares, "new pu1_5 to pu2_5_3")

squares.add_lines("2", "A", [0.5, 0, 0.5, 1, 'd'], printed_label="")
squares.remove_line("3:A")
squares.remove_line("A:3")
squares.remove_line("A:2")
squares.add_lines("A", "B", [0.5, 0, 0.5, 1, 'd'], printed_label="")
squares.remove_line("B:A")
squares.remove_square("2")
squares.remove_square("3")
squares.remove_square("B")

octic_squares2pdf(squares, "new pu1_5 to pu2_5_4")

squares.add_square("5'")
squares.remove_line("1:45")
squares.remove_line("4:15")
squares.remove_line("5:14")
squares.add_lines("1", "5'", [0, 0.8, 1, 0.8])
squares.add_lines("4", "5'", [0, 0.8, 1, 0.8])
squares.add_lines("5", "5'", [0, 0.8, 1, 0.8])

squares.add_lines("5'", "1", [0, 0.2, 1, 0.2])
squares.add_lines("5'", "4", [0, 0.5, 1, 0.5])
squares.add_lines("5'", "5", [0, 0.8, 1, 0.8])

squares.add_lines("A", "5'", [0.14, 0.4, 0.26, 0.6, 'd'], txt_offset=(-4,0))

octic_squares2pdf(squares, "new pu1_5 to pu2_5_5")

# squares.remove_line("A:1")
# squares.remove_line("A:2")
# squares.remove_line("A:3")
# squares.add_lines("A", "B", [0.5, 0, 0.5, 1, 'd'], printed_label="")
# squares.add_lines("1", "A", [0.5, 0, 0.5, 1, 'd'], printed_label="")
# squares.add_lines("3", "A", [0.5, 0, 0.5, 1, 'd'], printed_label="")
# squares.add_lines("4", "A", [0.5, 0, 0.5, 1, 'd'], printed_label="")
# squares.add_lines("5", "A", [0.5, 0, 0.5, 1, 'd'], printed_label="")
# squares.remove_line("A:4")
# squares.remove_line("A:5")
# squares.remove_line("B:A")
