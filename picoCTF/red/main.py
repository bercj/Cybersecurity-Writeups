from PIL import Image

def extract_lsb_from_channel(channel):
    bits = []
    for pixel in channel.getdata():
        bits.append(pixel & 1)  # get the least significant bit

    # Group bits into bytes
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        byte_val = 0
        for bit in byte:
            byte_val = (byte_val << 1) | bit
        if byte_val == 0:
            break  # stop at null byte
        chars.append(chr(byte_val))
    return ''.join(chars)

# Load image
img = Image.open("red.png")
r, g, b, *a = img.split()

flag_text = extract_lsb_from_channel(r)
print("Extracted from Red channel LSB:", flag_text)
