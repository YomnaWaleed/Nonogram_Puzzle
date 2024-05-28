import cv2
import numpy as np
White = (255, 255, 255)
Black = (0, 0, 0)
Line_offset = 25

def print_rectangels(img, offset, cell_unit, N, solution):
    """
    Prints the rectangles of the black cells on the figure
    :param img: the object of the image
    :param offset: offset of the drawing to leave area to the clues
    :param cell_unit: the lenght of the side of the cell
    :param N: the lenght of the side of the puzzle
    :param solution: the sent solution
    :return: img: the final object of the image
    """
    for row in range(N):
        for col in range(N):
            img = cv2.rectangle(img, # the image object
                                (offset+col*cell_unit, offset+row*cell_unit), # start position
                                (offset+(col+1)*cell_unit, offset+(row+1)*cell_unit), # end position
                                White if solution[row][col] == 0 else Black, # color
                                -1) # fill if -1 and line width if another positive value

            if solution[row][col] == 1:
              img = cv2.rectangle(img, # the image object
                                  (offset+col*cell_unit, offset+row*cell_unit), # start position
                                  (offset+(col+1)*cell_unit, offset+(row+1)*cell_unit), # end position
                                  White, # color
                                  8) # fill if -1 and line width if another positive value
    return img

def print_lines(img, offset, cell_unit, N, solution):
    """
        Prints the seperating lines on the figure
        :param img: the object of the image
        :param offset: offset of the drawing to leave area to the clues
        :param cell_unit: the lenght of the side of the cell
        :param N: the lenght of the side of the puzzle
        :param solution: the sent solution
        :return: img: the final object of the image
    """
    size = 750
    for row in range(N + 1):
        img = cv2.line(img,  # the image object
                       (offset + row * cell_unit, Line_offset),  # start position
                       (offset + row * cell_unit, size),  # end position
                       Black,  # color
                       2 if (row == N) else 1)

    for col in range(N + 1):
        img = cv2.line(img,  # the image object
                       (Line_offset, offset + col * cell_unit),  # start position
                       (size, offset + col * cell_unit),  # end position
                       Black,  # color
                       2 if (col == N) else 1)  # fill if -1 and line width if another positive value

    img = cv2.line(img,  # the image object
                   (offset, Line_offset),  # start position
                   (offset, size),  # end position
                   Black,  # color
                   2)
    img = cv2.line(img,  # the image object
                   (Line_offset, offset),  # start position
                   (size, offset),  # end position
                   Black,  # color
                   2)
    # first col
    img = cv2.line(img,  # the image object
                   (Line_offset, offset),  # start position
                   (Line_offset, size),  # end position
                   Black,  # color
                   2)
    # first row
    img = cv2.line(img,  # the image object
                   (offset, Line_offset),  # start position
                   (size, Line_offset),  # end position
                   Black,  # color
                   2)
    return img

def print_row_clues(img, offset, cell_unit, N, solution, row_clues):
    """
        Prints the rectangles of the black cells on the figure
        :param img: the object of the image
        :param offset: offset of the drawing to leave area to the clues
        :param cell_unit: the lenght of the side of the cell
        :param N: the lenght of the side of the puzzle
        :param solution: the sent solution
        :param row_clues: the clues on the side
        :return: img: the final object of the image
    """
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # text type
    Text_offset = int(250 / N)
    for i in range(N):
        for j in range(len(row_clues[i])):
              cv2.putText(img, # image object
                          str(row_clues[i][j]),
                          (Text_offset*(j+1),offset+i*cell_unit+int(cell_unit/2)), # start position (horizontal offset + cell offset + centering offset, vertical offset)
                          font, # font type
                          6/N, # size
                          Black, # color
                          1) #linewidth

def print_col_clues(img, offset, cell_unit, N, solution, col_clues):
    """
        Prints the rectangles of the black cells on the figure
        :param img: the object of the image
        :param offset: offset of the drawing to leave area to the clues
        :param cell_unit: the lenght of the side of the cell
        :param N: the lenght of the side of the puzzle
        :param solution: the sent solution
        :param col_clues: the clues above
        :return: img: the final object of the image
    """
    Text_offset = int(250 / N)
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # font type
    for i in range(N):
        for j in range(len(col_clues[i])):
          cv2.putText(img, # image object
                      str(col_clues[i][j]),
                      (offset+i*cell_unit+int(cell_unit/2), Line_offset+Text_offset*(j+1)), # start position(horizontal offset+cell offset+centering offset, Line offset+vertical offset)
                      font, # font type
                      6/N, # size
                      Black, # color
                      1) # line width
