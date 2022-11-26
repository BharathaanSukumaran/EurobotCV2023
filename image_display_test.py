
import cv2 as cv
import sys


# Read image from folder
img = cv.imread(cv.samples.findFile("images/output_sample.png"))

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)

# Display while user hasn't pressed a key
key = cv.waitKey(0)

# If the key is S write to the desired location
if key == ord("s"):
    cv.imwrite("image_read_write_test.png", img)