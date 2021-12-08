import cv2
import sys
import os
import numpy as np
import utlis


def Scanner(path_input_img, path_output_img, file_name):
    image = cv2.imread(os.path.join(path_input_img, file_name))
    # resize image so it can be processed
    # choose optimal dimensions such that important content is not lost
    image = cv2.resize(image, (1500, 880))

    # creating copy of original image
    orig = image.copy()

    # convert to grayscale and blur to smooth
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # blurred = cv2.medianBlur(gray, 5)

    # apply Canny Edge Detection
    edged = cv2.Canny(blurred, 0, 50)
    orig_edged = edged.copy()

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    (contours, _) = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # x,y,w,h = cv2.boundingRect(contours[0])
    # cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),0)

    # get approximate contour
    for c in contours:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)

        if len(approx) == 4:
            target = approx
            break

    # mapping target points to 800x800 quadrilateral
    approx = utlis.rectify(target)
    pts2 = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])

    # part 6 : Defining a transformation matrix
    M = cv2.getPerspectiveTransform(approx, pts2)

    # part 7 : Transformation on the input image
    dst = cv2.warpPerspective(orig, M, (800, 800))

    cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    # using thresholding on warped image to get scanned effect (If Required)
    ret, th1 = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    ret2, th4 = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # cv2.imshow("Original.jpg", orig)
    # cv2.imshow("Original Gray.jpg", gray)
    # cv2.imshow("Original Blurred.jpg", blurred)
    # cv2.imshow("Original Edged.jpg", orig_edged)
    # cv2.imshow("Outline.jpg", image)
    # cv2.imshow("Thresh Binary.jpg", th1)
    # cv2.imshow("Thresh mean.jpg", th2)
    # cv2.imshow("Thresh gauss.jpg", th3)
    # cv2.imshow("Otsu's.jpg", th4)
    # cv2.imshow("dst.jpg", dst)
    cv2.imwrite(os.path.join(path_output_img, file_name), dst)
    # print the result
    print("Created Image: " + os.path.join(path_output_img, file_name))
    # other thresholding methods


if __name__ == "__main__":
    # check if the input is correct , if not print suitable sentence
    if len(sys.argv) < 3:
        print("Missing Input/Output images!")
    else:
        # print the income Directories
        print("path_input_img:" + sys.argv[1])
        print("path_output_img:" + sys.argv[2])
        # loop for to run the function and print the result for each image
        for file_name in os.listdir(sys.argv[1]):
            Scanner(sys.argv[1], sys.argv[2], file_name)
