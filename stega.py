
# "Stegasaurus" by Prof. Tallman on Feb 8, 2024
# Code is based on recollections of my UOP senior project from 2004
# However, this time around I took some inspiration from Devang Jain
# on reshaping the pixels to a flat array (he seems to have gone 3D to 2D).
# https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2


from PIL import Image
import numpy as np


def hide_message(image:Image, message:bytes):
    """
    Hides a message inside of an image using LSb steganography.

    Args:
      - image: a PIL Image object to hide the message inside
      - message: the secret data as a byte string
    
    Returns a PIL image containing the hidden message with the same
    dimensions and visually indistinguishable from the original.
    """
    
    # Convert RGB image pixels to list [R1, G1, B1, R2, G2, B2, ...]
    pixels = np.array(image).astype(np.uint8)
    height, width, channels = pixels.shape
    flat_pixels = pixels.reshape(height*width*channels)
    
    # Convert to list of binary values and prepend message size
    data_bits = _bytes_to_bit_array(message)
    size_bits = np.array(len(data_bits)).astype(np.uint8).tobytes()
    size_bits = _bytes_to_bit_array(size_bits)
    data_bits = size_bits + data_bits
    
    # Hide the message in the pixel data
    hidden = _hide_message(flat_pixels, data_bits)

    # Convert pixel list back to a valid image file
    pixels = hidden.reshape(height, width, channels)
    image = Image.fromarray(pixels.astype(np.uint8))
    
    return image


def extract_message(image:Image):
    """
    Retrieves a message inside of an image using LSb steganography.

    Args:
      - image: a PIL Image object with a hidden message inside
    
    Returns a secret message from the least-significant-bits of the image.
    """

    # Convert RGB image pixels to list [R1, G1, B1, R2, G2, B2, ...]
    pixels = np.array(image).astype(np.uint8)
    height, width, channels = pixels.shape
    flat_pixels = pixels.reshape(height*width*channels)

    # Hide the message in the pixel data
    extracted = _extract_message(flat_pixels)

    # Convert the list of binary values back to a chunk of secret data
    datalen = int.from_bytes(_bit_array_to_bytes(extracted[:8]))
    databits = extracted[8:8+datalen]
    message = _bit_array_to_bytes(databits)
    return message


def _hide_message(pixels:np.array, data_bits:list):
    """
    Hides a message inside of an image using LSb steganography.

    Args:
      - pixels: a flat sequence of RGB values from a picture
      - data_bits: the secret data, a list of integers with value 0 or 1
    
    Returns a 3D Numpy Array containing the hidden message with the same
    dimensions and visually indistinguishable from the original.
    """
    if any(db > 1 or db < 0 for db in data_bits):
        raise ValueError(f"Data contains non-binary values")
    
    # Embed 1 bit of the secret data with each byte from the image, using LSB
    for idx in range(len(data_bits)):
        bit = data_bits[idx]
        if bit == 1:
            pixels[idx] = pixels[idx] | 0x01
        else:
            pixels[idx] = pixels[idx] & 0xFE  
    return pixels


def _extract_message(pixels:np.array):
    """
    Retrieves a message inside of an image using LSb steganography.

    Args:
      - pixels: a digital picture stored as a 3D numpy array
    
    Returns a secret message from the least-significant-bits of the image.
    """

    # Form the secret data by extracting 1 bit per byte of pixel data
    data_bits = []
    for idx in range(len(pixels)):
        if pixels[idx] & 0x01 == 1:
            data_bits += [1]
        else:
            data_bits += [0]
    return data_bits


def _bytes_to_bit_array(byte_string:bytes):
    """ 
    Converts a byte string into an array of bits (e.g., a list of
    integers 0/1).
    
    For example:
      - _bytes_to_bit_array(b"\x00") => [0, 0, 0, 0, 0, 0, 0, 0] 
      - _bytes_to_bit_array(b"\x05") => [0, 0, 0, 0, 0, 1, 0, 1] 
      - _bytes_to_bit_array(b"\xFF") => [1, 1, 1, 1, 1, 1, 1, 1] 
    """
    bit_count = len(byte_string) * 8
    result = [0] * bit_count
    idx = 0
    for byte in byte_string:
        for bit_pos in [7,6,5,4,3,2,1,0]:
            mask = 1 << bit_pos
            if byte & mask > 0:
                result[idx] = 1
            idx += 1
    return result


def _bit_array_to_bytes(bit_array):
    """ 
    Converts an array of bits (list of integers 0/1) into a byte string.
    
    For example:
      - _bit_array_to_bytes([0, 0, 0, 0, 0, 0, 0, 0]) => b"\x00"
      - _bit_array_to_bytes([0, 0, 0, 0, 0, 1, 0, 1]) => b"\x05"
      - _bit_array_to_bytes([1, 1, 1, 1, 1, 1, 1, 1]) => b"\xFF"
    """
    result = []
    byte = 0
    for idx, bit in enumerate(bit_array):
        pos = idx % 8
        byte += bit << (7 - pos)
        if pos == 7:
            result += [byte]
            byte = 0
    return bytes(result)


def main():
    import argparse
    from os import path

    desc = '''Hides secret message in pictures. If a message is included, then
            the message is embedded inside of the picture. If the message is 
            omitted, a message is extracted from the picture. Messages that are
            extracted from benign images will be gibberish.
            
            When embedding a secret message, the color of each pixel is changed
            slightly but not in a way that is discernable to viewers. The image
            will be saved as a PNG file using the original file (overwriting
            the original image in the process).  '''
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-f', '--file', type=str, help='JPEG or PNG file', required=True)
    parser.add_argument('-m', '--message', type=str, help='The secret message', required=False)
    args = parser.parse_args()

    if not path.exists(args.file):
        print(f"Error: {args.file} does not exist")
        return
    
    # insert message into file
    if args.message:
        message = args.message.encode('utf-8')
        image = Image.open(args.file)
        image = hide_message(image, message)
        image.save(args.file, "PNG")
    
    # no secret message, extract a message from the file
    else:
        image = Image.open(args.file)
        secret = extract_message(image)
        secret = secret.decode('utf-8')
        print(secret)


if __name__ == '__main__':
    main()