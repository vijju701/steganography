from PIL import Image

def genData(data):
    return [format(ord(i), '08b') for i in data]

def modPix(pix, data):
    datalist = genData(data)
    imdata = iter(pix)

    for i, byte in enumerate(datalist):
        # 3×3 = 9 pixels per byte
        pixel_block = [v for _ in range(3) for v in imdata.__next__()[:3]]

        for bit_index in range(8):
            if byte[bit_index] == '0' and pixel_block[bit_index] % 2:
                pixel_block[bit_index] -= 1
            elif byte[bit_index] == '1' and pixel_block[bit_index] % 2 == 0:
                pixel_block[bit_index] = pixel_block[bit_index] - 1 if pixel_block[bit_index] else 1

        # end‑marker
        if i == len(datalist) - 1:
            pixel_block[-1] = pixel_block[-1] - 1 if pixel_block[-1] % 2 == 0 else pixel_block[-1]
        else:
            pixel_block[-1] = pixel_block[-1] - 1 if pixel_block[-1] % 2 else pixel_block[-1]

        yield from [tuple(pixel_block[j:j+3]) for j in range(0, 9, 3)]

def encode_enc(img, data):
    w = img.size[0]
    x = y = 0
    for pixel in modPix(img.getdata(), data):
        img.putpixel((x, y), pixel)
        x, y = (0, y + 1) if x == w - 1 else (x + 1, y)

def encode():
    src = input("Carrier image (with extension): ")
    img = Image.open(src).convert("RGB")

    secret = input("Message to hide: ")
    if not secret:
        raise ValueError("No data!")

    out_name = input("Output image name (e.g. secret.png): ")
    new_img = img.copy()
    encode_enc(new_img, secret)
    new_img.save(out_name, out_name.split('.')[-1].upper())
    print(f"Saved → {out_name}")

def decode():
    src = input("Image to read: ")
    img = Image.open(src).convert("RGB")

    data, imgdata = '', iter(img.getdata())
    while True:
        pixels = [v for _ in range(3) for v in imgdata.__next__()[:3]]
        byte = ''.join('0' if p % 2 == 0 else '1' for p in pixels[:8])
        data += chr(int(byte, 2))
        if pixels[-1] % 2:  # stop flag
            return data

def main():
    choice = input("1) Encode\n2) Decode\n> ")
    if choice == '1':
        encode()
    elif choice == '2':
        print("Decoded:", decode())
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
