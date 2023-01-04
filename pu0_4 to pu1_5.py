from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5, _IMG_SIZE=(800, 120))
# xyz(x+y+z)(x-y+w)=0

squares.add_lines("1", "25", [0, 0.5, 1, 0.5])
squares.add_lines("1", "3", [0, 0, 1, 1])
squares.add_lines("1", "4", [0, 1, 1, 0])

squares.add_lines("2", "15", [0, 0.5, 1, 0.5])
squares.add_lines("2", "3", [0, 0, 1, 1])
squares.add_lines("2", "4", [0, 1, 1, 0])

squares.add_lines("3", "1", [0.5, 0, 0.5, 1])
squares.add_lines("3", "2", [0, 0.5, 1, 0.5])
squares.add_lines("3", "4", [0, 1, 1, 0])
squares.add_lines("3", "5", [0, 0, 1, 1])

squares.add_lines("4", "1", [0.5, 0, 0.5, 1])
squares.add_lines("4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("4", "3", [0, 1, 1, 0])
squares.add_lines("4", "5", [0, 0, 1, 1])

squares.add_lines("5", "12", [0, 0.5, 1, 0.5])
squares.add_lines("5", "3", [0, 0, 1, 1])
squares.add_lines("5", "4", [0, 1, 1, 0])

octic_squares2pdf(squares, "pu0_4 to pu1_5_0")

squares.add_lines("", "5'", [0.5, 0, 0.5, 1], squares=["1", "2", "3", "4", "5"], dashed=True, printed_label="5")

squares.add_lines("1", "25", [0, 0.5, 1, 0.5])
squares.add_lines("1", "3", [0, 0.3, 1, 0.3])
squares.add_lines("1", "4", [0, 0.7, 1, 0.7])

squares.add_lines("2", "15", [0, 0.5, 1, 0.5])
squares.add_lines("2", "3", [0, 0.3, 1, 0.3])
squares.add_lines("2", "4", [0, 0.7, 1, 0.7])

squares.add_lines("3", "1", [0, 0.2, 1, 0.2])
squares.add_lines("3", "2", [0, 0.4, 1, 0.4])
squares.add_lines("3", "4", [0, 0.6, 1, 0.6])
squares.add_lines("3", "5", [0, 0.8, 1, 0.8])

squares.add_lines("4", "1", [0, 0.2, 1, 0.2])
squares.add_lines("4", "2", [0, 0.4, 1, 0.4])
squares.add_lines("4", "3", [0, 0.6, 1, 0.6])
squares.add_lines("4", "5", [0, 0.8, 1, 0.8])

squares.add_lines("5", "12", [0, 0.5, 1, 0.5])
squares.add_lines("5", "3", [0, 0.3, 1, 0.3])
squares.add_lines("5", "4", [0, 0.7, 1, 0.7])

squares.add_square("5'")

squares.add_lines("5'", "1", [0.7, 0, 0.3, 1])
squares.add_lines("5'", "2", [0.3, 0, 0.7, 1])
squares.add_lines("5'", "3", [1, 0.3, 0.2, 1], txt_offset=[3, 0])
squares.add_lines("5'", "4", [0, 0.3, 0.8, 1])
squares.add_lines("5'", "5", [0, 0.5, 1, 0.5])

octic_squares2pdf(squares, "pu0_4 to pu1_5_1")

squares.add_lines("", "a", [0.33, 0.25, 0.57, 0.45], dashed=True, printed_label="", squares=["1", "2"])
squares.mark_no_intersection("1", "3", "5'")
squares.mark_no_intersection("2", "3", "5'")

squares.add_lines("", "b", [0.33, 0.65, 0.57, 0.85], dashed=True, printed_label="", squares=["1", "2"])
squares.mark_no_intersection("1", "4", "5'")
squares.mark_no_intersection("2", "4", "5'")

squares.remove_line("5':3")
squares.remove_line("5':4")
squares.remove_line("3:5")
squares.remove_line("4:5")
squares.remove_line("3:5'")
squares.remove_line("4:5'")
squares.remove_line("5:3")
squares.remove_line("5:4")

squares.add_lines("", "5'", [0.5, 0, 0.5, 1], squares=["3", "4"], dashed=True, printed_label="")

octic_squares2pdf(squares, "pu0_4 to pu1_5_2")

squares.remove_line("1:3")
squares.remove_line("1:4")
squares.remove_line("2:3")
squares.remove_line("2:4")
squares.remove_square("3")
squares.remove_square("4")

octic_squares2pdf(squares, "pu0_4 to pu1_5_3")

squares.remove_line("1:25")
squares.remove_line("2:15")
squares.remove_line("5:12")
squares.remove_line("5':1")
squares.remove_line("5':2")
squares.remove_line("5':5")

squares.add_square("2'")
squares.add_lines("2'", "1", [0, 0.3, 1, 0.3])
squares.add_lines("2'", "2", [0, 0.5, 1, 0.5])
squares.add_lines("2'", "5", [0, 0.7, 1, 0.7])
squares.add_lines("2'", "5'", [0.5, 0, 0.5, 1], printed_label="5")
squares.add_lines("1","5'",[0.5,0,0.5,1], dashed=True,printed_label="")
squares.add_lines("","2'",[0,0.5,1,0.5],squares=["1","2","5"], printed_label="2")

# squares.add_lines("5'","1",[0,0.3,1,0.3])
squares.add_lines("5'","2",[0,0.5,1,0.5])
squares.add_lines("5'","5",[0,0.7,1,0.7])
squares.add_lines("5'","2'",[0.5,0,0.5,1],dashed=True,printed_label="2")
octic_squares2pdf(squares, "pu0_4 to pu1_5_4")
