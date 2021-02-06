import sys
from skimage import io


def convert():
    filepath = sys.argv[1]
    image = io.imread(filepath, as_gray=True)
    height, width = image.shape
    resize_height_factor = 1
    resize_width_factor = 1
    if height > 1000:
        resize_height_factor += height // 1000
    if width > 1000:
        resize_width_factor += width // 1000
    result = open("output.txt", "w")
    for row in range(0, height, 3 * resize_height_factor):
        for col in range(0, width, 1 * resize_width_factor):
            result.write(get_character(image[row, col]))
        result.write("\n")


def get_character(pixel):
    if pixel == 1.0:
        return " "
    elif pixel > 0.95:
        return "."
    elif pixel > 0.88:
        return ":"
    elif pixel > 0.75:
        return "~"
    elif pixel > 0.63:
        return "+"
    elif pixel > 0.43:
        return "I"
    elif pixel > 0.3:
        return "#"
    elif pixel > 0.2:
        return "%"
    elif pixel > 0.1:
        return "B"
    else:
        return "@"


if __name__ == '__main__':
    convert()
