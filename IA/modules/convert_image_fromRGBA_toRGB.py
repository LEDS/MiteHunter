from types import NoneType
from PIL import Image

def convert_image_RGBA_RGB(filename) -> None:
    """
    Feature: Function responsible for converting 4-channel images (RGBA) to 3 channels (RGB).

    @param: 
        - filename: str.
    
    @return: None
    """

    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        image = Image.open(filename)
        if image.mode == 'RGBA':
            image = image.convert('RGB')
            image.save(filename)
        else:
            pass
    else:
        raise ValueError(f"Imagem com tipo inesperado. O tipo desta imagem é {filename.endswith}.")