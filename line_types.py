from octic_config import *

GRID =[
    0,SQUARE_SIZE/4,SQUARE_SIZE/2,3*SQUARE_SIZE/4,SQUARE_SIZE
]
SS = SQUARE_SIZE

#each line type returns a triple: (line_start, line_end, text_pos)
def middle_vertical():
    return(
        (SS/2, 0),
        (SS/2, SS),
        (SS/2 + LINE_W_OFFSET, LINE_H_OFFSET + FONT_SIZE)
    )

def middle_horizontal():
    return(
        (0, SS/2),
        (SS, SS/2),
        (LINE_W_OFFSET, SS/2 - LINE_H_OFFSET - 1)
    )

def main_diag():
    return(
        (0, 0),
        (SS, SS),
        (LINE_W_OFFSET + 8, LINE_H_OFFSET + FONT_SIZE)
    )

def opp_diag():
    return(
        (0, SS),
        (SS, 0),
        (8+LINE_W_OFFSET, SS - LINE_H_OFFSET - 1)
    )

def top14_left34():
    return(
        (SS/4, 0),
        (SS, 3*SS/4),
        (SS/4 + 8 + LINE_W_OFFSET, LINE_H_OFFSET + FONT_SIZE)
    )

def right34_top34():
    return(
        (0, 3*SS/4),
        (3*SS/4, 0),
        (4 + LINE_W_OFFSET, 3*SS/4)
    )

def top14_left34():
    return(
        (SS/4, 0),
        (SS, 3*SS/4),
        (SS/4 + 8 + LINE_W_OFFSET, LINE_H_OFFSET + FONT_SIZE)
    )

def right34_top34():
    return(
        (0, 3*SS/4),
        (3*SS/4, 0),
        (4 + LINE_W_OFFSET, 3*SS/4)
    )

def top17_bot57():
        return(
        (SS/7, 0),
        (5*SS/7, SS),
        (SS/7 + 4 + LINE_W_OFFSET, LINE_H_OFFSET + FONT_SIZE)
    )

def top67_bot27():
        return(
        (6*SS/7, 0),
        (2*SS/7, SS),
        (6*SS/7 + LINE_W_OFFSET, LINE_H_OFFSET + FONT_SIZE)
    )

line_styles = {
    "mv":middle_vertical,
    "mh":middle_horizontal,
    "md":main_diag,
    "od":opp_diag,
    "t14_l34":top14_left34,
    "r34_t34":right34_top34,
    "t17_b57":top17_bot57,
    "t67_b27":top67_bot27
    }