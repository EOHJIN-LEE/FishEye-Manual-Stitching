import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

# img1 = cv2.imread('1.jpg', -1)  # queryImage
# img2 = cv2.imread('2.jpg', -1)  # trainImage

num = 0
img_x = 0
img_y = 0
flagbool = False

w, h = 2, 4
pts1 = [[0 for x in range(w)] for y in range(h)]
pts2 = [[0 for x in range(w)] for y in range(h)]


def mouse_callback_xy(event, x, y, flags, param):
    global num
    global img_x
    global img_y
    global flagbool

    if event == cv2.EVENT_LBUTTONDOWN:
        # pts1[num][0] = x
        # pts1[num][1] = y
        img_x = x
        img_y = y
        num = num + 1
        flagbool = True


def pickme(string, img1, img2, direction):
    print('-------------------pickme_start-----------------')
    # total_num = len(src_pts)

    # width, height = 2, total_num
    if direction is "right":
        img0 = img1
        img1 = img2
        img2 = img0

    img3 = img1.copy()
    img4 = img2.copy()

    global num
    # global temp1, temp2
    # temp1 = [[0 for x in range(width)] for y in range(height)]
    # temp2 = [[0 for x in range(width)] for y in range(height)]

    # number = 0

    # for i in range(total_num):
    #     if matchesMask[i] == 1:
    #         temp1[number][0] = int(src_pts[i][0][0])
    #         temp1[number][1] = int(src_pts[i][0][1])
    #         temp2[number][0] = int(dst_pts[i][0][0])
    #         temp2[number][1] = int(dst_pts[i][0][1])
    #         number += 1

    # print(temp1)

    cv2.namedWindow(string)
    cv2.setMouseCallback(string, mouse_callback_xy)
    cv2.imshow(string, img1)

    global pts1, pts2, flagbool

    k1 = []
    k2 = []

    while True:
        k = cv2.waitKey(1) & 0xFF
        if flagbool:
            # pts1[num-1][0] = img_x
            # pts1[num-1][1] = img_y
            k1.append([])
            k1[num-1].append(img_x)
            k1[num-1].append(img_y)
            cv2.circle(img3, (img_x, img_y), 3, (0, 0, 255), -1)
            flagbool = False
             # if num == 4:
             #     break

        if k == 27:
                break

    print(len(k1))
    cv2.imshow('please', img3)
    # cv2.circle(img1, (pts1[0][0], pts1[0][1]), 3, (0, 0, 255), -1)

    cv2.destroyWindow(string)
    print('************did1')






    cv2.namedWindow(string)
    cv2.setMouseCallback(string, mouse_callback_xy)
    cv2.imshow(string, img2)

    num = 0

    while True:
        k = cv2.waitKey(1) & 0xFF
        if flagbool:
            # pts2[num - 1][0] = img_x
            # pts2[num - 1][1] = img_y
            k2.append([])
            k2[num-1].append(img_x)
            k2[num-1].append(img_y)
            cv2.circle(img4, (img_x, img_y), 3, (0, 0, 255), -1)
            print(num)
            print(len(k1))
            flagbool = False

        if num == len(k1):
            break

    cv2.destroyWindow(string)

    cv2.imshow('please', img4)

    print('************did2')





    if direction is "left":
        pts1 = k1
        pts2 = k2
    elif direction is "right":
        pts1 = k2
        pts2 = k1

    num = 0

    print(pts1)
    print(pts2)

    # if tf:
    #     remember = 1.0e+20
    #     global remember_num
    #     remember_num = 0
    #
    #     for j in range(4):
    #         for i in range(total_num):
    #             if remember > (math.pow(temp1[i][0] - pts1[j][0], 2) + math.pow(temp1[i][1] - pts1[j][1], 2)):
    #                 remember_num = i
    #                 remember = math.pow(temp1[i][0] - pts1[j][0], 2) + math.pow(temp1[i][1] - pts1[j][1], 2)
    #
    #         pts1[j][0] = temp1[remember_num][0]
    #         pts1[j][1] = temp1[remember_num][1]
    #         pts2[j][0] = temp2[remember_num][0]
    #         pts2[j][1] = temp2[remember_num][1]
    #         remember_num = 0
    #         remember = 1.0e+20
    #
    #     print(pts1)

    print('imfree')

    # cv2.namedWindow(string)
    # cv2.setMouseCallback(string, mouse_callback_xy)
    #
    # cv2.imshow(string, img1)
    #
    # num = 0
    #
    # while(1):
    #         cv2.imshow('image', img1)
    #         k = cv2.waitKey(1) & 0xFF
    #
    #         if num == 1:
    #             Matrix[0][0] = img_x
    #             Matrix[0][1] = img_y
    #
    #         elif num == 2:
    #             Matrix[1][0] = img_x
    #             Matrix[1][1] = img_y
    #
    #         elif num == 3:
    #             Matrix[2][0] = img_x
    #             Matrix[2][1] = img_y
    #
    #         elif num == 4:
    #             Matrix[3][0] = img_x
    #             Matrix[3][1] = img_y
    #
    #         elif k == 27:
    #             break
    #
    # print(Matrix)
    # cv2.destroyWindow(string)
    #
    # cv2.namedWindow(string)
    # cv2.setMouseCallback('image2', mouse_callbackxy)
    #
    # while(1):
    #     cv2.imshow('image2', img2)
    #     k = cv2.waitKey(1) & 0xFF
    #
    #     if num2 == 1:
    #         Matrix2[0][0] = img_x
    #         Matrix2[0][1] = img_y
    #     elif num2 == 2:
    #         Matrix2[1][0] = img_x
    #         Matrix2[1][1] = img_y
    #
    #     elif num2 == 3:
    #         Matrix2[2][0] = img_x
    #         Matrix2[2][1] = img_y
    #
    #     elif num2 == 4:
    #         Matrix2[3][0] = img_x
    #         Matrix2[3][1] = img_y
    #
    #     elif k == 27:
    #         break
    #
    # cv2.destroyWindow('image2')
    #
    # print(Matrix)
    # print(Matrix2)
    #
    # pts1 = np.float32(Matrix)
    # pts2 = np.float32(Matrix2)
    #
    # M = cv2.getPerspectiveTransform(pts1, pts2)
    # print(M)
    # dst = cv2.warpPerspective(img2, M, (1280,250))
    #
    # b, g, r = cv2.split(dst)  # img파일을 b,g,r로 분리
    # newdst = cv2.merge([r, g, b])  # b, r을 바꿔서 Merge
    #
    #
    # plt.imshow(newdst)
    # plt.title('Perspective')
    # plt.show()

    return pts1, pts2
