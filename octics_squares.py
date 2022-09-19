import svgwrite
from line_types import line_styles
from octic_config import *

def draw_square(dwg,pos,txt):
    dwg.add(dwg.rect(
        insert=pos,
        size=(SQUARE_SIZE,SQUARE_SIZE),
        stroke="black",
        stroke_width=SQUARE_STROKE,
        fill="white"))
    dwg.add(dwg.text(
        txt,
        insert=(
            pos[0]+SQUARE_SIZE/2-5,
            pos[1]+SQUARE_SIZE+SQ_TEXT_OFFSET),
        style = FONT_STYLE))

def add_line(dwg,pos,txt,style):
    line_poss = line_styles[style]()
    dwg.add(dwg.line(
        start=(pos[0]+line_poss[0][0],line_poss[0][1]+pos[1]),
        end=(pos[0]+line_poss[1][0],line_poss[1][1]+pos[1]),
        stroke_width=1,
        stroke="black")
        )
    dwg.add(dwg.text(
        txt,
        insert=(pos[0]+line_poss[2][0],pos[1]+line_poss[2][1]),
        style = FONT_STYLE))

class OcticSquares:
    def __init__(self,filename,num_of_squares):
        self.num_of_squares = num_of_squares
        self.dwg = svgwrite.Drawing(filename = filename, size = IMG_SIZE)

        self.squares = {}
        self.curr_pos = (LEFT_OFFSET,TOP_OFFSET)
        for i in range(1,num_of_squares+1):
            sq_id="P"+str(i)
            draw_square(self.dwg,self.curr_pos,sq_id)
            self.squares[sq_id]=self.curr_pos
            self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET,self.curr_pos[1])

    def add_lines(self,squares,label,style):
        for square in squares:
            add_line(self.dwg,self.squares[square],label,style)

    def add_square(self,label):
        draw_square(self.dwg,self.curr_pos,label)
        self.squares[label]=self.curr_pos
        self.curr_pos = (self.curr_pos[0] + SQUARE_SIZE + SQUARE_OFFSET,self.curr_pos[1])

    def save(self):
        self.dwg.save()

    