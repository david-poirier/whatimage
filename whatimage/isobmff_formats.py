
def _identify_heic(major_brand, minor_version, compatible_brands):
    container_brands = [b'mif1',b'msf1']
    coding_brands = [b'heic',b'heix',b'hevc',b'hevx']
    if major_brand in coding_brands:
        return 'heic'
    if major_brand in container_brands:
        for cb in compatible_brands: 
            if cb in coding_brands:
                return 'heic'


def _identify_avif(major_brand, minor_version, compatible_brands):
    container_brands = [b'mif1',b'msf1']
    coding_brands = [b'avif',b'avis']
    if major_brand in coding_brands:
        return 'avif'
    if major_brand in container_brands:
        for cb in compatible_brands: 
            if cb in coding_brands:
                return 'avif'


def identify_isobmff(data):
    if len(data) < 8:
        return
    if data[4:8] != b'ftyp':
        return
    ftyp_len = int.from_bytes(data[0:4], 'big')
    if len(data) < ftyp_len:
        return
    major_brand = data[8:12]
    minor_version = int.from_bytes(data[12:16], 'big')
    compatible_brands = []
    for offset in range(16, ftyp_len, 4):
        compatible_brands.append(data[offset:offset+4])

    for func in [_identify_heic, _identify_avif]:
        fmt = func(major_brand, minor_version, compatible_brands)
        if fmt:
            return fmt

