from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(4)

# u^2 = x y z (x+y+z+w)
# STEP 0 - p04 point
squares.add_lines("P1", "2", [0, 0, 1, 1])
squares.add_lines("P1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("P1", "4", [0, 1, 1, 0])

squares.add_lines("P2", "1", [0, 0, 1, 1])
squares.add_lines("P2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("P2", "4", [0, 1, 1, 0])

squares.add_lines("P3", "1", [0, 0, 1, 1])
squares.add_lines("P3", "2", [0, 0.5, 1, 0.5])
squares.add_lines("P3", "4", [0, 1, 1, 0])

squares.add_lines("P4", "1", [0, 0, 1, 1])
squares.add_lines("P4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("P4", "3", [0, 1, 1, 0])

octic_squares2pdf(squares, "new pu0_4_0")

# STEP 1 - blow-up of L_{12}
squares.remove_line("P1:2")
squares.remove_line("P2:1")
squares.add_lines("P3", "4a", [0.5, 0, 0.5, 1, 'd'], printed_label="4")
squares.add_lines("P4", "3a", [0.5, 0, 0.5, 1, 'd'], printed_label="3")

squares.remove_line("P4:1")
squares.add_lines("P4", "1", [0, 0.2, 1, 0.2])
squares.remove_line("P3:1")
squares.add_lines("P3", "1", [0, 0.2, 1, 0.2])

squares.remove_line("P4:3")
squares.add_lines("P4", "3", [0, 0.8, 1, 0.8])
squares.remove_line("P3:4")
squares.add_lines("P3", "4", [0, 0.8, 1, 0.8])

octic_squares2pdf(squares, "new pu0_4_1")

# STEP 2 - blow-up of L_{13}
squares.remove_line("P1:3")
squares.remove_line("P3:1")
squares.add_lines("P4", "4a", [0.4, 0.1, 0.6, 0.3, 'd'], printed_label= "")
octic_squares2pdf(squares, "new pu0_4_2")

# STEP 3 - blow-up of L_{23}
squares.remove_line("P2:3")
squares.remove_line("P3:2")
squares.add_lines("P4", "4b", [0.4, 0.4, 0.6, 0.6, 'd'], printed_label= "")
octic_squares2pdf(squares, "new pu0_4_3")

# STEP 4 - blow-up of L_{14} and L_{24}
squares.remove_line("P1:4")
squares.remove_line("P4:1")
squares.remove_line("P2:4")
squares.remove_line("P4:2")
octic_squares2pdf(squares, "new pu0_4_4")
