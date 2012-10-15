# SYSC 2004 A Fall 2011 Lab 5

import CU_picture
import filters


def get_picture():
    """
    Interactively select a picture file and return it.
    """

    # Pop up a dialogue box to select a file
    file = CU_picture.choose_file()

    # Open the file containing the picture and load it
    pict = CU_picture.load_picture(file)

    return pict

if __name__ == "__main__":
   pass

 