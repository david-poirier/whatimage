from .simple_formats import *
from .isobmff_formats import *

identify_functions = [
        identify_jpeg,
        identify_png,
        identify_gif,
        identify_webp,
        identify_isobmff,
        identify_bmp,
        identify_tiff,
        identify_pbm,
        identify_pgm,
        identify_ppm]

def identify_image(data):
    for func in identify_functions:
        fmt = func(data)
        if fmt:
            return fmt

