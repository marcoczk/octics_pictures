from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# xyz(x+y+wz)(x+wy+z)=0

squares.add_lines("1", "24", [0, 0, 1, 1])
squares.add_lines("1", "35", [0, 1, 1, 0])

squares.add_lines("2", "14", [0, 0, 1, 1])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "5", [0, 1, 1, 0])

squares.add_lines("3", "15", [0, 0, 1, 1])
squares.add_lines("3", "2", [0, 0.5, 1, 0.5])
squares.add_lines("3", "4", [0, 1, 1, 0])

squares.add_lines("4", "12", [0, 0, 1, 1])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "5", [0, 1, 1, 0])

squares.add_lines("5", "13", [0, 0, 1, 1])
squares.add_lines("5", "2", [0, 0.5, 1, 0.5])
squares.add_lines("5", "4", [0, 1, 1, 0])

octic_squares2pdf(squares, "pu0_5 to pu2_5_0")

squares.add_square("E")

squares.add_lines("1", "24", [0, 0.4, 1, 0.4])
squares.add_lines("1", "35", [0, 0.6, 1, 0.6])
# squares.add_lines("1", "E", [0.5, 0, 0.5, 1])

squares.add_lines("2", "14", [0, 0.3, 1, 0.3])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "5", [0, 0.7, 1, 0.7])
# squares.add_lines("2", "E", [0.5, 0, 0.5, 1])

squares.add_lines("3", "15", [0, 0.3, 1, 0.3])
squares.add_lines("3", "2", [0, 0.5, 1, 0.5])
squares.add_lines("3", "4", [0, 0.7, 1, 0.7])
# squares.add_lines("3", "E", [0.5, 0, 0.5, 1])

squares.add_lines("4", "12", [0, 0.3, 1, 0.3])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "5", [0, 0.7, 1, 0.7])
# squares.add_lines("4", "E", [0.5, 0, 0.5, 1])

squares.add_lines("5", "13", [0, 0.3, 1, 0.3])
squares.add_lines("5", "2", [0, 0.5, 1, 0.5])
squares.add_lines("5", "4", [0, 0.7, 1, 0.7])
# squares.add_lines("5", "E", [0.5, 0, 0.5, 1])

squares.add_lines("", "E", [0.5, 0, 0.5, 1], dashed=True, squares=["1", "2", "3", "4", "5"])

squares.add_lines("E", "1", [0, 0.5, 1, 0.5])
squares.add_lines("E", "2", [0, 1, 1, 0])
squares.add_lines("E", "3", [0.1, 0, 0.3, 1])
squares.add_lines("E", "4", [0, 0, 1, 1], txt_offset=[-2, 0])
squares.add_lines("E", "5", [0.3, 0, 0.1, 1])

octic_squares2pdf(squares, "pu0_5 to pu2_5_1")

squares.add_lines("1", "E", [0.5, 0, 0.5, 1], dashed=True, printed_label="")
squares.add_lines("2", "4a", [0.33, 0.25, 0.57, 0.45], dashed=True, printed_label="4", txt_offset=[0, -2])
squares.add_lines("3", "5a", [0.33, 0.25, 0.57, 0.45], dashed=True, printed_label="5", txt_offset=[0, -2])
squares.add_lines("4", "2a", [0.33, 0.25, 0.57, 0.45], dashed=True, printed_label="2", txt_offset=[0, -2])
squares.add_lines("5", "3a", [0.33, 0.25, 0.57, 0.45], dashed=True, printed_label="3", txt_offset=[0, -2])
squares.mark_no_intersection("2", "14", "E")
squares.mark_no_intersection("3", "15", "E")
squares.mark_no_intersection("4", "12", "E")
squares.mark_no_intersection("5", "13", "E")
squares.remove_line("E:1")

octic_squares2pdf(squares, "pu0_5 to pu2_5_2")

squares.remove_square("E")
squares.add_lines("", "b", [0.33, 0.45, 0.57, 0.65], dashed=True, printed_label="", squares=["2", "3", "4", "5"])
squares.add_lines("", "c", [0.33, 0.65, 0.57, 0.85], dashed=True, printed_label="", squares=["2", "3", "4", "5"])
squares.add_lines("", "E", [0.5, 0, 0.5, 1], dashed=True, squares=["2", "3", "4", "5"], printed_label="")

squares.mark_no_intersection("2", "3", "E")
squares.mark_no_intersection("2", "5", "E")
squares.mark_no_intersection("3", "2", "E")
squares.mark_no_intersection("3", "4", "E")
squares.mark_no_intersection("4", "3", "E")
squares.mark_no_intersection("4", "5", "E")
squares.mark_no_intersection("5", "2", "E")
squares.mark_no_intersection("5", "4", "E")

octic_squares2pdf(squares, "pu0_5 to pu2_5_3")

squares.remove_line("2:3")
squares.remove_line("3:2")
squares.remove_line("2:5")
squares.remove_line("5:2")
squares.remove_line("4:3")
squares.remove_line("3:4")
squares.remove_line("4:5")
squares.remove_line("5:4")

octic_squares2pdf(squares, "pu0_5 to pu2_5_4")

squares.add_square("2'")
squares.add_square("3'")

squares.remove_line("1:24")
squares.remove_line("1:35")
squares.remove_line("2:14")
squares.remove_line("3:15")
squares.remove_line("4:12")
squares.remove_line("5:13")
squares.add_lines("1", "2", [0, 0.4, 1, 0.4])
squares.add_lines("1", "3", [0, 0.6, 1, 0.6])
squares.add_lines("2", "2", [0, 0.3, 1, 0.3])
squares.add_lines("3", "3", [0, 0.3, 1, 0.3])
squares.add_lines("4", "2", [0, 0.3, 1, 0.3])
squares.add_lines("5", "3", [0, 0.3, 1, 0.3])
squares.mark_no_intersection("2", "2", "E")
squares.mark_no_intersection("3", "3", "E")
squares.mark_no_intersection("4", "2", "E")
squares.mark_no_intersection("5", "3", "E")
squares.add_lines("2'", "1", [0, 0.3, 1, 0.3])
squares.add_lines("2'", "2", [0, 0.5, 1, 0.5])
squares.add_lines("2'", "4", [0, 0.7, 1, 0.7])
squares.add_lines("3'", "1", [0, 0.3, 1, 0.3])
squares.add_lines("3'", "3", [0, 0.5, 1, 0.5])
squares.add_lines("3'", "5", [0, 0.7, 1, 0.7])

octic_squares2pdf(squares, "pu0_5 to pu2_5_5")
