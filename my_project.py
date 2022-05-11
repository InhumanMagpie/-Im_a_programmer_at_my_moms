import os
import sys


from PIL import Image

try:
    im = Image.open("Lenna_(test_image).png")
except FileNotFoundError:
    print("Файл не найден")

print("Размер изображения:")
print(im.format, im.size, im.mode)

# im.show()


for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
