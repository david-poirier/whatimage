
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

