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
squares.add_lines("5", "4", [0, 0, 1, 1])

octic_squares2pdf(squares, "pu0_5 to pu1_5_0")

squares.add_square("E")

squares.add_lines("1", "24", [0, 0.3, 1, 0.3])
squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("1", "5", [0, 0.7, 1, 0.7])

squares.add_lines("2", "14", [0, 0.3, 1, 0.3])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "5", [0, 0.7, 1, 0.7])

squares.add_lines("3", "1", [0, 0.2, 1, 0.2])
squares.add_lines("3", "2", [0, 0.4, 1, 0.4])
squares.add_lines("3", "4", [0, 0.6, 1, 0.6])
squares.add_lines("3", "5", [0, 0.8, 1, 0.8])

squares.add_lines("4", "12", [0, 0.3, 1, 0.3])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "5", [0, 0.7, 1, 0.7])

squares.add_lines("5", "1", [0, 0.2, 1, 0.2])
squares.add_lines("5", "2", [0, 0.4, 1, 0.4])
squares.add_lines("5", "3", [0, 0.6, 1, 0.6])
squares.add_lines("5", "4", [0, 0.8, 1, 0.8])

squares.add_lines("", "E", [0.5, 0, 0.5, 1], dashed=True, squares=["1", "2", "3", "4", "5"])

squares.add_lines("E", "1", [0.7, 0, 0.3, 1])
squares.add_lines("E", "2", [0.3, 0, 0.7, 1])
squares.add_lines("E", "3", [1, 0.3, 0.2, 1], txt_offset=[3, 0])
squares.add_lines("E", "4", [0, 0.5, 1, 0.5])
squares.add_lines("E", "5", [0, 0.3, 0.8, 1])

octic_squares2pdf(squares, "pu0_5 to pu1_5_1")

squares.add_lines("2", "4a", [0.33, 0.25, 0.57, 0.45], printed_label="4", dashed=True, txt_offset=[0, -2])
squares.add_lines("4", "2a", [0.33, 0.25, 0.57, 0.45], printed_label="2", dashed=True, txt_offset=[0, -2])

squares.remove_line("1:E")
squares.remove_line("2:E")
squares.remove_line("3:E")
squares.remove_line("4:E")
squares.remove_line("5:E")
squares.remove_square("E")

octic_squares2pdf(squares, "pu0_5 to pu1_5_2")

squares.add_square("2'")

squares.remove_line("1:24")
squares.remove_line("2:14")
squares.remove_line("4:12")
squares.add_lines("1", "2'", [0, 0.3, 1, 0.3])
squares.add_lines("2", "2'", [0, 0.3, 1, 0.3])
squares.add_lines("4", "2'", [0, 0.3, 1, 0.3])
squares.add_lines("2'", "1", [0, 0.3, 1, 0.3])
squares.add_lines("2'", "2", [0, 0.5, 1, 0.7])
squares.add_lines("2'", "4", [0, 0.7, 1, 0.5])

octic_squares2pdf(squares, "pu0_5 to pu1_5_3")
