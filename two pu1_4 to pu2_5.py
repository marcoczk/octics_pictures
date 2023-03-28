from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# x y (x+y) z (x+z+w)=0


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

octic_squares2pdf(squares, "two pu1_4 to pu2_5_0")

squares.add_square("E")

squares.remove_line("1:23")
squares.remove_line("2:13")
squares.remove_line("3:12")

squares.add_lines("1", "E", [0, 0, 1, 1])
squares.add_lines("2", "E", [0, 0, 1, 1])
squares.add_lines("3", "E", [0, 0, 1, 1])

squares.add_lines("4", "2", [0, 0.2, 1, 0.2])
squares.add_lines("4", "3", [0, 0.5, 1, 0.5])
squares.add_lines("4", "15", [0, 0.8, 1, 0.8])
squares.add_lines("4", "5E", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("5", "2", [0, 0.2, 1, 0.2])
squares.add_lines("5", "3", [0, 0.5, 1, 0.5])
squares.add_lines("5", "14", [0, 0.8, 1, 0.8])
squares.add_lines("5", "4E", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("E", "1", [0, 0.2, 1, 0.2])
squares.add_lines("E", "2", [0, 0.5, 1, 0.5])
squares.add_lines("E", "3", [0, 0.8, 1, 0.8])
squares.add_lines("E", "45", [0.5, 0, 0.5, 1])

octic_squares2pdf(squares, "two pu1_4 to pu2_5_1")

squares.remove_line("1:E")
squares.remove_line("2:E")
squares.remove_line("3:E")
squares.remove_line("E:1")
squares.remove_line("E:2")
squares.remove_line("E:3")

squares.add_lines("4", "5a", [0.35, 0.15, 0.6, 0.4], dashed=True, printed_label="5", txt_offset=(-5, 0))
squares.add_lines("4", "5b", [0.35, 0.45, 0.6, 0.7], dashed=True, printed_label="5", txt_offset=(-5, 0))
squares.add_lines("4", "5c", [0.35, 0.75, 0.6, 1], dashed=True, printed_label="5", txt_offset=(-5, 0))
squares.add_lines("5", "4a", [0.35, 0.15, 0.6, 0.4], dashed=True, printed_label="4", txt_offset=(-5, 0))
squares.add_lines("5", "4b", [0.35, 0.45, 0.6, 0.7], dashed=True, printed_label="4", txt_offset=(-5, 0))
squares.add_lines("5", "4c", [0.35, 0.75, 0.6, 1], dashed=True, printed_label="4", txt_offset=(-5, 0))
squares.mark_no_intersection("4","2","5E")
squares.mark_no_intersection("4","3","5E")
squares.mark_no_intersection("4","15","5E")
squares.mark_no_intersection("5","2","4E")
squares.mark_no_intersection("5","3","4E")
squares.mark_no_intersection("5","14","4E")

octic_squares2pdf(squares, "two pu1_4 to pu2_5_2")

squares.remove_line("2:4")
squares.remove_line("2:5")
squares.remove_line("3:4")
squares.remove_line("3:5")
squares.remove_line("4:2")
squares.remove_line("4:3")
squares.remove_line("5:2")
squares.remove_line("5:3")

squares.remove_square("2")
squares.remove_square("3")
# squares.add_lines("4", "4a", [0.445, 0.08, 0.445, 0.28], dashed=True, printed_label="")
# squares.add_lines("4", "4b", [0.445, 0.38, 0.445, 0.58], dashed=True, printed_label="")
# squares.add_lines("5", "5a", [0.445, 0.08, 0.445, 0.28], dashed=True, printed_label="")
# squares.add_lines("5", "5b", [0.445, 0.38, 0.445, 0.58], dashed=True, printed_label="")

octic_squares2pdf(squares, "two pu1_4 to pu2_5_3")

squares.remove_line("1:45")
squares.remove_line("4:15")
squares.remove_line("5:14")

squares.add_square("5'")
squares.add_lines("1", "5'", [0, 1, 1, 0])
squares.add_lines("4", "5'", [0, 0.8, 1, 0.8])
squares.add_lines("5", "5'", [0, 0.8, 1, 0.8])
squares.add_lines("5'", "1", [0,0.3,1,0.3])
squares.add_lines("5'", "4", [0, 0.7, 1, 0.5])
squares.add_lines("5'", "5", [0, 0.5, 1, 0.7])
squares.mark_no_intersection("5","5'","4E")
squares.mark_no_intersection("4","5'","5E")

octic_squares2pdf(squares, "two pu1_4 to pu2_5_4")


squares.remove_line("5:4E")
squares.remove_line("4:5E")
squares.remove_line("E:45")
squares.add_square("4'")
squares.add_lines("E","4'", [0.5,0,0.5,1])
squares.add_lines("4", "4'", [0.5, 0, 0.5, 1], dashed=True)
squares.add_lines("5", "4'", [0.5, 0, 0.5, 1], dashed=True)
squares.add_lines("4'", "E", [0, 0.3, 1, 0.3])

squares.add_lines("4'", "4", [0, 0.5, 0.338, 0.7])
squares.add_lines("4'", "5", [0, 0.7, 0.338, 0.5])
squares.add_lines("4'", "4a", [0.325, 0.7, 0.665, 0.5],printed_label="")
squares.add_lines("4'", "5a", [0.325, 0.5, 0.665, 0.7],printed_label="")
squares.add_lines("4'", "4b", [0.655, 0.5, 1, 0.7],printed_label="")
squares.add_lines("4'", "5b", [0.655, 0.7, 1, 0.5],printed_label="")
squares.mark_no_intersection("4","5'","4'")
squares.mark_no_intersection("5","5'","4'")


octic_squares2pdf(squares, "two pu1_4 to pu2_5_5")

squares.remove_square("1")
squares.remove_square("E")
squares.remove_line("5':1")
squares.remove_line("4':E")

octic_squares2pdf(squares, "two pu1_4 to pu2_5_6")
