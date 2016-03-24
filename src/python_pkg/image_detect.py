#!/usr/bin/env python

import numpy as np
import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image


#def get_image():
 #   retval, im = camera.read()
  #  return im

def detect_image(image):

    detect = False
    ramp_frames = 30
    flag = False
    print "Inside detect IMAGE"
    #hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   
    #camera = cv2.VideoCapture(0)
    #del (camera)
    # define range of red color in HSV
    # lower mask (0-10)
    lower_red0 = np.array([0,50,50])
    upper_red0 = np.array([10,255,255])

    # upper mask (170-180)
    lower_red1 = np.array([170,50,50])
    upper_red1 = np.array([180,255,255])
    #camera = cv2.VideoCapture(0)
    for x in range(0, 3):
        frame = image
	lower_red = np.array([0,50,50], dtype=np.uint8)
	upper_red = np.array([180,255,255], dtype=np.uint8)
	
        img_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
        mask = cv2.inRange(img_hsv, lower_red, upper_red)
        detect=np.any(mask,None,None,False)
    
    if detect == True:
        for i in xrange(ramp_frames):
	    temp = image
	result = "Found"
        print ("Object found")
        print ("Taking image...")
        # Take the actual image
        camera_capture = image
        file = "/home/garima/Pictures/test_image.png"
        flag = cv2.imwrite(file, camera_capture)
        print ("Image taken")
        img3=cv2.imread('/home/garima/Pictures/test_image.png')
        cv2.imshow('Original',img3)
        
    if detect == False:
	result = "Not_Found"
        flag= False
        print ("Object not Found")

    del(image)

    if flag == True:
        img = cv2.imread('/home/garima/Pictures/test_image.png')
        img_hsv2=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask0 = cv2.inRange(img_hsv2, lower_red0, upper_red0)
        mask1 = cv2.inRange(img_hsv2, lower_red1, upper_red1)

        # join my masks
        mask = mask0+mask1
        output_hsv = img_hsv2.copy()
        output_hsv[np.where(mask==0)] = 0
        red = cv2.bitwise_and(img,img, mask= mask)
        file = "/home/garima/Pictures/test_imagemask.png"
        cv2.imwrite(file, red)
        img2=cv2.imread('/home/garima/Pictures/test_imagemask.png')
        print img2
        cv2.imshow('Mask',img2)
        image_data_red = img2[:,:,:]
        median_red = np.median(image_data_red)
        columns = np.where(image_data_red.max(axis=0)>median_red)[0]
        rows = np.where(image_data_red.max(axis=1)>median_red)[0]
        tuplered = (min(rows), max(rows), min(columns), max(columns))
        x = tuplered[0]
        print tuplered
        print x
        if x < 100:
	    print ("Object in the left")
        if x > 100:
	    print ("Objet in the right")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return result
