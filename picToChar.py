from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def size_input():
    return 75
    # return int(input("picture size :"))


def file_input():
    # return input("image file path:")
    return "yang2.jpg"


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    if r > 235 and g > 235 and b > 235:
        r, g, b = 255, 255, 255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_char[int(gray / 257 * length)]


if __name__ == '__main__':
    im = Image.open(file_input())  # type:Image.Image
    size = size_input()
    old_x, old_y = im.size
    new_x = 2*size * old_x // old_y
    im = im.resize((new_x, size))
    txt = ""
    for y in range(size):
        for x in range(new_x):
            rgb = im.getpixel((x, y))
            # print(rgb)
            txt += get_char(*rgb)
        txt += '\n'
    print(txt)
    with open("picChar.txt", 'w') as f:
        f.write(txt)
