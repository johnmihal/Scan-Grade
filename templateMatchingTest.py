from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#get image input and convert to grayscale.
img = cv.imread('Images/sheet1.jpg')
img = cv.resize(img, (600, 1000))
img_bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Get marker image aopencvnd convert to grayscale
#template = cv.imread('Images/scantronTemplate.jpg')
#temp_bw = cv.cvtColor(template, cv.COLOR_BGR2GRAY)


#Initailizes ORB object
#orb = cv.ORB_create()

#Finds keypoints and descriptors for both images
#imgKP, imgDesc = orb.detectAndCompute(img_bw, None)
#tempKP, tempDesc = orb.detectAndCompute(temp_bw, None)


#Matches keypoints
#matcher = cv.BFMatcher()
#matches = matcher.match(imgDesc, tempDesc)

#final_img = cv.drawMatches(img_bw, imgKP, temp_bw, tempKP, matches, None)

#final_img = cv.resize(final_img, (1000,650))

#cv.imshow("Matches", final_img)
#cv.waitKey(3000)

#Blurs the image slightly
blurred = cv.GaussianBlur(img_bw, (5, 5), 0)

#finds edges of the image
edged = cv.Canny(blurred, 75, 200)

cv.imshow("image", edged) 
cv.waitKey(0)

#Finds contours in the edge map, then initializes the contour that corresponds to the document
conts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
conts = imutils.grab_contours(conts)
docCont = None

#ensure at least on contour was found
if len(conts) > 0:
    #sort contours
    conts = sorted(conts, key=cv.contourArea, reverse=True)

    for c in conts:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, .02 * peri, True)

        if(len(approx) == 4):
            docCont = approx
            break

cv.drawContours(img, docCont, -1, (0, 255, 0), 3)
plt.figure()
cv.imshow("image", img)

cv.waitKey(0)