The author's contact information Name: Ahmed Alshafaee , 
Extract Handwriting from Background My goal is to remove the
Yellow background and keep only the handwriting in front

Building a document scanner with OpenCV can be accomplished in just six steps:

1. using (Banalization) thresholding on warped image to get scanned effect
2. find the contours in the edged image, keeping only the largest ones, and initialize the screen contour
3. Using "Peucker–Douglas–Ramer" algorithm to bring the contour closer by four points. it's implemented in the "
   cv2.approxPolyDP" function. 
4. after we have the image edges we want to find the image Shapes 
5. Defining a transformation matrix
6. Transformation on the input image

Warning : you may have Warning "Cannot find reference 'imread' in '__init__.py | __init__
   .py'" , its just bug in pycharm , the Program will run normally

use this command to run the Program, i have to include the Input and the Outputs folders for segmentation each image
from Input folder and the result well be seen in Output folder , and the code is in background_remove.py python3

I used pycharm , to run the program , first you have to install this packages below in terminal:

1.run  "pip install -r requirements.txt" to install the packages

2.run "python3  background_remove.py Input\ images/ Outputs/"
 
bellow we can see before and after implementing the code in image
![before](https://user-images.githubusercontent.com/58431974/145190076-d48dfe7f-9eb2-469a-9415-614bdd9f7da6.jpg)
![after](https://user-images.githubusercontent.com/58431974/145190094-08bcf17b-2c1a-4e66-a0cb-56e70d4bb381.jpg)
