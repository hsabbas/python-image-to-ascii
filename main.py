import sys
from skimage import io


def convert():
    filepath = sys.argv[1]
    image = io.imread(filepath, as_gray=True)
    height, width = image.shape
    result = open("output.txt", "w")
    for row in range(0, height, 2):
        for col in range(width):
            average_pixel_value = (image[row, col] + image[row + 1, col]) / 2
            result.write(get_character(average_pixel_value))
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
