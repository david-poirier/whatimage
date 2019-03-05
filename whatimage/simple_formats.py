def identify_tiff(data):
    if len(data) < 4:
        return
    if data[0:2] == b'MM':
        if int.from_bytes(data[2:4], byteorder='big') == 42:
            return 'tiff'
    if data[0:2] == b'II':
        if int.from_bytes(data[2:4], byteorder='little') == 42:
            return 'tiff'


def identify_bmp(data):
    if len(data) < 2:
        return
    if data[0:2] == b'BM':
        return 'bmp'


def identify_pbm(data):
    if len(data) < 2:
        return
    if data[0:2] == b'P4':
        return 'pbm'


def identify_pgm(data):
    if len(data) < 2:
        return
    if data[0:2] == b'P5':
        return 'pgm'


def identify_ppm(data):
    if len(data) < 2:
        return
    if data[0:2] == b'P6':
        return 'ppm'


def identify_gif(data):
    if len(data) < 6:
        return None
    if data[:6] in [b'GIF87a', b'GIF89a']:
        return 'gif'


def identify_png(data):
    if len(data) < 4:
        return None
    if data[0] == 0x89 and data[1:4] == b'PNG':
        return 'png'


def identify_jpeg(data):
    if len(data) < 3:
        return None
    if data[0] == 0xff \
            and data[1] == 0xd8 \
            and data[2] == 0xff:
        return 'jpeg'

def identify_webp(data):
    if len(data) < 12:
        return None
    if data[0:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'

