from PIL import Image
import os

def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save("Images/" + filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                print("fail")
                pass

def main():
    print("hello")
    imgcrop("Images/gridTest1.png",4,8)

if __name__ == "__main__":
    main()