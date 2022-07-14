import PIL
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

# crops answer bullets
def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input[input.find('/'):])
    im = PIL.Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces

    #   output array
    rows, cols = (yPieces,xPieces)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0, rows):
        for j in range(0, cols):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                #a.save("Images/Split/" + filename + "-" + str(i) + "-" + str(j) + file_extension)
                lumosity = brightness(a)

                if lumosity > 117:
                    arr[i][j] = 0 # 0 = blank
                else:
                    arr[i][j] = 1 # 1 = filled
            except Exception as err:
                print(err)
                pass
    return arr

#   Returns Greyscale Brightness 255 = white, 0 = black
def brightness(a):
   im = a.convert('L')
   stat = PIL.ImageStat.Stat(im)
   return stat.mean[0]

#   coordinates the data collection from the input image
def getInput(img, col, row):
    answers = imgcrop("Images/gridTest1.png", col, row)
    return answers

# Loads the test answer key
def loadAnswerKey(col, row):
    key = [[0 for i in range(col)] for j in range(row)]

    for j in range(0, row):
        key[j][0] = 1
    return key

# grades the test
def grade(key, input, col, row):
    for i in range(0, row):
        correct = True
        for j in range(0, col):
            if key[i][j] != input[i][j]:
                correct = False
        if correct:
            print(i+1, " Correct")
        else:
            print(i+1, " Incorrect")


def main():
    print(os.getcwd())  # this tells you what directory you are running from, good for debugging.

    # These indicate the number of questions as row and the number of
    # potential answers per question is col
    col = 4
    row = 8

    key = loadAnswerKey(col, row)
    print(key)
    input = getInput("Images/gridTest1.png", col, row)
    print(input)
    grade(key, input, col, row)


class ScanGradeUI(Widget):
    pass

class ScanGrade(App):
    def build(self):
        return ScanGradeUI()

if __name__ == "__main__":
    main()
    ScanGrade().run()