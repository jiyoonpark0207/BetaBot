#!/usr/bin/env python

import numpy as np
import cv2
import time

gx = 0
gy = 0

from Motor import *
bb = Motor()

from random import seed, randint


from Ultrasonic import * #import Led


def dist():
    ultrasonic = Ultrasonic()  # create an object
    data = ultrasonic.get_distance()  # Get the value
    print("Obstacle distance is " + str(data) + "CM")
    return data


def betabot_nav(x, y):
    d = dist()
    print("distance: %s" % d)
    if d > 30:
        # Ab.forward()
        # time.sleep(2)
        # Ab.stop()
        if x > 65:
            print("move right")
            bb.right()
            time.sleep(1)
            bb.stop()
        elif x < 35:
            print("move left")
            bb.left()
            time.sleep(1)
            bb.stop()
        else:
            print("move forward")
            bb.forward()
            time.sleep(1)
            bb.stop()
    else:
        print("stop")
        bb.stop()


def read_rgb_image(image_name, show):
    rgb_image = cv2.imread(image_name)
    if show:
        cv2.imshow("RGB Image", rgb_image)
    return rgb_image


def filter_color(rgb_image, lower_bound_color, upper_bound_color):
    # convert the image into the HSV color space
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv image", hsv_image)

    # define a mask using the lower and upper bounds of the yellow color
    mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)

    return mask


def getContours(binary_image):
    # _, contours, hierarchy = cv2.findContours(binary_image,
    #                                          cv2.RETR_TREE,
    #                                           cv2.CHAIN_APPROX_SIMPLE)
    _, contours, hierarchy = cv2.findContours(binary_image.copy(),
                                              cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_SIMPLE)
    return contours


def draw_ball_contour(binary_image, rgb_image, contours):
    global gx, gy
    black_image = np.zeros([binary_image.shape[0], binary_image.shape[1], 3], 'uint8')

    for c in contours:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if (area > 3000):
            cv2.drawContours(rgb_image, [c], -1, (150, 250, 150), 1)
            cv2.drawContours(black_image, [c], -1, (150, 250, 150), 1)
            cx, cy = get_contour_center(c)
            # print(cx, cy)
            gx = cx
            gy = cy
            cv2.circle(rgb_image, (cx, cy), (int)(radius), (0, 0, 255), 1)
            cv2.circle(black_image, (cx, cy), (int)(radius), (0, 0, 255), 1)
            cv2.circle(black_image, (cx, cy), 5, (150, 150, 255), -1)
            # print ("Area: {}, Perimeter: {}".format(area, perimeter))
        else:
            gx = -100
            gy = -100
    # print ("number of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours", rgb_image)
    cv2.imshow("Black Image Contours", black_image)


def get_contour_center(contour):
    M = cv2.moments(contour)
    cx = -1
    cy = -1
    if (M['m00'] != 0):
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    return cx, cy


def detect_ball_in_a_frame(image_frame):
    yellowLower = (30, 100, 50)
    yellowUpper = (60, 255, 255)
    rgb_image = image_frame
    binary_image_mask = filter_color(rgb_image, yellowLower, yellowUpper)
    contours = getContours(binary_image_mask)
    draw_ball_contour(binary_image_mask, rgb_image, contours)


def main():
    video_capture = cv2.VideoCapture(0)
    # video_capture = cv2.VideoCapture('video/tennis-ball-video.mp4')
    width = video_capture.get(3)  # float `width`
    height = video_capture.get(4)

    while (True):
        ret, frame = video_capture.read()
        detect_ball_in_a_frame(frame)
        time.sleep(0.033)
        if gx > 0:
            print((gx / width) * 100, (gy / height) * 100)
            alphabot_nav(gx, 0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()