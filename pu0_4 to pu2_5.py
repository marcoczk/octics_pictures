from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# x y z (x+y+z) (x+y+w)=0


squares.add_lines("1", "25", [0, 0, 1, 1])
squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("1", "4", [0, 1, 1, 0])

squares.add_lines("2", "15", [0, 0, 1, 1])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "4", [0, 1, 1, 0])

squares.add_lines("3", "2", [0, 0, 1, 1])
squares.add_lines("3", "1", [0, 0.5, 1, 0.5])
squares.add_lines("3", "45", [0, 1, 1, 0])

squares.add_lines("4", "2", [0, 0, 1, 1])
squares.add_lines("4", "1", [0, 0.5, 1, 0.5])
squares.add_lines("4", "35", [0, 1, 1, 0])

squares.add_lines("5", "12", [0, 0, 1, 1])
squares.add_lines("5", "34", [0, 1, 1, 0])

octic_squares2pdf(squares, "new pu0_4 to pu2_5_0")

squares.add_lines("1", "25", [0, 0.3, 1, 0.3])
squares.add_lines("1", "3", [0, 0.5, 1, 0.5])
squares.add_lines("1", "4", [0, 0.7, 1, 0.7])
squares.add_lines("1", "5'", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("2", "15", [0, 0.3, 1, 0.3])
squares.add_lines("2", "3", [0, 0.5, 1, 0.5])
squares.add_lines("2", "4", [0, 0.7, 1, 0.7])
squares.add_lines("2", "5'", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("3", "2", [0, 0.3, 1, 0.3])
squares.add_lines("3", "1", [0, 0.5, 1, 0.5])
squares.add_lines("3", "45", [0, 0.7, 1, 0.7])
squares.add_lines("3", "5'", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("4", "2", [0, 0.3, 1, 0.3])
squares.add_lines("4", "1", [0, 0.5, 1, 0.5])
squares.add_lines("4", "35", [0, 0.7, 1, 0.7])
squares.add_lines("4", "5'", [0.5, 0, 0.5, 1], dashed=True)

squares.add_lines("5", "12", [0, 0.4, 1, 0.4])
squares.add_lines("5", "34", [0, 0.6, 1, 0.6])
squares.add_lines("5", "5'", [0.5, 0, 0.5, 1], dashed=True)

squares.add_square("5'")

squares.add_lines("5'", "1", [0, 0, 1, 1], txt_offset=(-2, 0))
squares.add_lines("5'", "2", [0, 1, 1, 0])
squares.add_lines("5'", "3", [0.3, 0, 0.1, 1])
squares.add_lines("5'", "4", [0.1, 0, 0.3, 1])
squares.add_lines("5'", "5", [0, 0.5, 1, 0.5])

octic_squares2pdf(squares, "new pu0_4 to pu2_5_1")

squares.remove_line("1:3")
squares.remove_line("1:4")
squares.remove_line("2:3")
squares.remove_line("2:4")
squares.remove_line("3:1")
squares.remove_line("3:2")
squares.remove_line("4:1")
squares.remove_line("4:2")

squares.mark_no_intersection("5'", "1", "4")
squares.mark_no_intersection("5'", "1", "3")
squares.mark_no_intersection("5'", "2", "4")
squares.mark_no_intersection("5'", "2", "3")

octic_squares2pdf(squares, "new pu0_4 to pu2_5_2")

squares.remove_line("1:25")
squares.remove_line("2:15")
squares.remove_line("5:12")
squares.add_lines("1", "5''", [0, 0.3, 1, 0.3])
squares.add_lines("2", "5''", [0, 0.3, 1, 0.3])
squares.add_lines("5", "5''", [0, 0.4, 1, 0.4])

squares.add_square("5''")
squares.add_lines("5''", "1", [0, 0.3, 1, 0.3])
squares.add_lines("5''", "2", [0, 0.5, 1, 0.5])
squares.add_lines("5''", "5", [0, 0.7, 1, 0.7])
squares.add_lines("5'", "5''", [0.6, 0.3, 0.6, 0.7], dashed=True, txt_offset=(2, -1))
squares.add_lines("5''", "5'", [0.5, 0, 0.5, 1])
squares.mark_no_intersection("5'", "1", "2")

octic_squares2pdf(squares, "new pu0_4 to pu2_5_3")

squares.remove_square("1")
squares.remove_square("2")

squares.remove_line("5'':1")
squares.remove_line("5'':2")
squares.remove_line("5':1")
squares.remove_line("5':2")

octic_squares2pdf(squares, "new pu0_4 to pu2_5_4")

squares.add_square("5'''")

squares.add_lines("5'''", "3", [0, 0.3, 1, 0.3])
squares.add_lines("5'''", "4", [0, 0.5, 1, 0.5])
squares.add_lines("5'''", "5", [0, 0.7, 1, 0.7])

squares.add_lines("5'", "5'''", [0.33, 0.45, 0.13, 0.75], dashed=True, txt_offset=(9, 0))
squares.mark_no_intersection("5'","3","4")
squares.add_lines("5'''", "5'", [0.5, 0, 0.5, 1])
squares.add_lines("5", "5'''", [0, 0.6, 1, 0.6], txt_offset=(4, 0))

squares.add_lines("3", "5'''", [0, 0.7, 1, 0.7], txt_offset=(4, 0))
squares.add_lines("4", "5'''", [0, 0.7, 1, 0.7], txt_offset=(4, 0))

squares.remove_line("3:45")
squares.remove_line("4:35")
squares.remove_line("5:34")

octic_squares2pdf(squares, "new pu0_4 to pu2_5_5")

squares.remove_square("3")
squares.remove_square("4")

squares.remove_line("5':3")
squares.remove_line("5':4")
squares.remove_line("5''':3")
squares.remove_line("5''':4")

octic_squares2pdf(squares, "new pu0_4 to pu2_5_6")
