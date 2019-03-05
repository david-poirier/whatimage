# whatimage
Python library to detect image type from a few bytes, focussed on webby formats (old and new)

Currently supports:
- JPEG
- WEBP
- GIF
- PNG
- HEIC
- AVIF
- BMP
- TIFF
- PBM/PGM/PPM


## Installation
```
pip install whatimage
```

## Usage
```python
import whatimage

with open('image.jpg', 'rb') as f:
    data = f.read()
fmt = whatimage.identify_image(data)
print(fmt)
```
> 'jpeg'

