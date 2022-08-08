import sys

def hexToRgb(hexcode):
    r = int(hexcode[:2], 16)
    g = int(hexcode[2:4], 16)
    b = int(hexcode[4:], 16)
    print(f"RGB of {hexcode}: ({r}, {g}, {b})")

def rgbToHex(r, g, b):
    if(int(r) > 255 or int(g) > 255 or int(b) > 255):
        print("RGB values should be between 0 and 255")
        sys.exit()
    rh = hex(int(r)).lstrip("0x")
    gh = hex(int(g)).lstrip("0x")
    bh = hex(int(b)).lstrip("0x")
    hexcode = rh.zfill(2) + gh.zfill(2) + bh.zfill(2)
    hexcode = hexcode.upper()

    print(f"Hexcode of ({r},{g},{b}): 0x{hexcode}")

if(len(sys.argv) == 2):
    hexToRgb(sys.argv[1])
elif(len(sys.argv) == 4):
    rgbToHex(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("usage: 1 hex code or 3 space-separated rbg values")
    sys.exit()

