from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# x y (x+y) z (x+y+z+w)=0


squares.add_lines("1", "23", [0, 0.5, 1, 0.5])
squares.add_lines("1", "4", [0, 1, 1, 0])
squares.add_lines("1", "5", [0, 0, 1, 1])

squares.add_lines("2", "13", [0, 0.5, 1, 0.5])
squares.add_lines("2", "4", [0, 1, 1, 0])
squares.add_lines("2", "5", [0, 0, 1, 1])

squares.add_lines("3", "12", [0, 0.5, 1, 0.5])
squares.add_lines("3", "4", [0, 1, 1, 0])
squares.add_lines("3", "5", [0, 0, 1, 1])

squares.add_lines("4", "1", [0.5, 0, 0.5, 1])
squares.add_lines("4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 1, 1, 0])
squares.add_lines("4", "5", [0, 0, 1, 1])

squares.add_lines("5", "1", [0.5, 0, 0.5, 1])
squares.add_lines("5", "2", [0, 0.5, 1, 0.5])
squares.add_lines("5", "3", [0, 1, 1, 0])
squares.add_lines("5", "4", [0, 0, 1, 1])

octic_squares2pdf(squares, "two pu1_4 to pu1_5_0")

squares.add_square("E")

squares.remove_lines(["1:23", "2:13", "3:12"])
squares.add_lines("", "E", [0, 0.5, 1, 0.5], squares=["1", "2", "3"])
squares.add_lines("E", "1", [0, 0.3, 1, 0.3])
squares.add_lines("E", "2", [0, 0.5, 1, 0.5])
squares.add_lines("E", "3", [0, 0.7, 1, 0.7])
squares.add_lines("E", "45", [0.5, 0, 0.5, 1])
squares.add_lines("5", "E4", [0.5, 0, 0.5, 1], dashed=True)
squares.add_lines("4", "E5", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("4", "1", [0, 0.2, 1, 0.2])
squares.add_lines("4", "2", [0, 0.4, 1, 0.4])
squares.add_lines("4", "3", [0, 0.6, 1, 0.6])
squares.add_lines("4", "5", [0, 0.8, 1, 0.8])

squares.add_lines("5", "1", [0, 0.2, 1, 0.2])
squares.add_lines("5", "2", [0, 0.4, 1, 0.4])
squares.add_lines("5", "3", [0, 0.6, 1, 0.6])
squares.add_lines("5", "4", [0, 0.8, 1, 0.8])

octic_squares2pdf(squares, "two pu1_4 to pu1_5_1")
# L_{14}, L_{15}, L_{1E}, L_{24}, L_{25}, L_{2E}, L_{35}, L_{34}, L_{3E}
squares.remove_square("1")
squares.remove_square("2")
squares.remove_square("3")

squares.remove_line("4:1")
squares.add_lines("5", "5a", [0.4, 0.1, 0.6, 0.3], dashed=True, printed_label="E", txt_offset=(-6,2))
squares.add_lines("E", "Ea", [0.35, 0.15, 0.65, 0.45], dashed=True, printed_label="5", txt_offset=(-5, 2))
squares.remove_line("5:1")
# squares.add_lines("E", "Eaa", [0.46, 0.15, 0.4, 0.33], dashed=True, printed_label="")
squares.remove_line("E:1")

squares.remove_line("4:2")
squares.add_lines("5", "5b", [0.4, 0.3, 0.6, 0.5], dashed=True, printed_label="E", txt_offset=(-6,2))
squares.add_lines("E", "Eb", [0.35, 0.35, 0.65, 0.65], dashed=True, printed_label="5", txt_offset=(-5, 2))
squares.remove_line("5:2")
# squares.add_lines("E", "Ebb", [0.46, 0.35, 0.4, 0.53], dashed=True, printed_label="")
squares.remove_line("E:2")

squares.remove_line("4:3")
squares.add_lines("5", "5c", [0.4, 0.5, 0.6, 0.7], dashed=True, printed_label="E", txt_offset=(-6,2))
squares.add_lines("E", "Ec", [0.35, 0.55, 0.65, 0.85], dashed=True, printed_label="5", txt_offset=(-5, 2))
squares.remove_line("5:3")
# squares.add_lines("E", "Ecc", [0.46, 0.55, 0.4, 0.73], dashed=True, printed_label="")
squares.remove_line("E:3")

octic_squares2pdf(squares, "two pu1_4 to pu1_5_2")

squares.add_square("5'")
squares.remove_line("4:E5")
squares.add_lines("4", "5'", [0.5, 0, 0.5, 1], dashed=True)
squares.remove_line("5:E4")
squares.add_lines("5", "5'", [0.5, 0, 0.5, 1], dashed=True)
squares.remove_line("E:45")
squares.add_lines("E", "5'", [0.5, 0, 0.5, 1])

# squares.add_lines("5'", "4", [0, 0.3, 1, 0.3])
# squares.add_lines("5'", "5", [0, 0.5, 1, 0.5])

squares.add_lines("5'", "E", [0, 0.5, 0.338, 0.7])
squares.add_lines("5'", "5", [0, 0.7, 0.338, 0.5])
squares.add_lines("5'", "Ea", [0.325, 0.7, 0.665, 0.5],printed_label="")
squares.add_lines("5'", "5a", [0.325, 0.5, 0.665, 0.7],printed_label="")
squares.add_lines("5'", "Eb", [0.655, 0.5, 1, 0.7],printed_label="")
squares.add_lines("5'", "5b", [0.655, 0.7, 1, 0.5],printed_label="")


squares.add_lines("5'", "4", [0, 0.3, 0.665, 0.3])
squares.add_lines("5'", "4a", [0.655, 0.3, 1, 0.6], printed_label="")

# squares.add_lines("5'", "5a", [0.3,0,0.3,1],printed_label="5")
# squares.add_lines("5'", "5b", [0.5,0,0.5,1],printed_label="5")
# squares.add_lines("5'", "5c", [0.7,0,0.7,1],printed_label="5")

octic_squares2pdf(squares, "two pu1_4 to pu1_5_3")

squares.remove_line("4:5")
squares.remove_line("4:5'")
squares.remove_line("5:4")
squares.remove_square("4")

squares.remove_line("5':4")
squares.remove_line("5':4a")

octic_squares2pdf(squares, "two pu1_4 to pu1_5_4")

#
# squares.add_lines("5'","4",[0,0.2,1,0.2])
# squares.add_lines("5'","5",[0,0.5,1,0.5])
# squares.add_lines("5'","E",[0,0.8,1,0.8])
#
# squares.remove_lines("4:E5")
# squares.remove_lines("5:E4")
# squares.remove_lines("E:45")
# squares.add_lines("E", "5", [0.5, 0, 0.5, 1], dashed=True)
# squares.add_lines("5", "5", [0.5, 0, 0.5, 1], dashed=True)
# squares.add_lines("4", "5", [0.5, 0, 0.5, 1], dashed=True)

# octic_squares2pdf(squares, "two pu1_4 to pu1_5_4")
