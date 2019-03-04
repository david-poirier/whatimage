from .simple_formats import *
from .isobmff_formats import *

def identify_image(data):
    for func in [identify_jpeg, identify_isobmff, identify_png, identify_gif]:
        fmt = func(data)
        if fmt:
            return fmt

