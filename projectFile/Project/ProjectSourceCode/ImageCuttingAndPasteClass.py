import numpy as np
from matplotlib import pyplot as plt
import cv2
import glob
import easygui

# img1 = cv2.imread('1.jpg', -1)    # queryImage
# img2 = cv2.imread('2222.jpg', -1) # trainImage
# img77 = cv2.imread('3.jpg', 0)
# img_first = cv2.imread('pig_checkerboard1', -1)
# img_second = cv2.imread('pig_checkerboard2', -1)

img_x = 100
img_y = 100

def mouse_callback(event,x,y,flags,param):
    global img_x

    if event == cv2.EVENT_LBUTTONDOWN:
        img_x = x
        print(img_x)


def mouse_callback_y(event,x,y,flags,param):

    global img_y

    if event == cv2.EVENT_LBUTTONDOWN:
        img_y = y
        print(img_y)


def CuttingAndPaste(img2_UnDistort, img3_UnDistort):
    # cv2.namedWindow('image')

    while True:

        cv2.setMouseCallback('image', mouse_callback)


        while(1):

            cv2.imshow('image', img2_UnDistort)
            k = cv2.waitKey(1) & 0xFF

            if k == ord('m'):
                drawing_mode = not drawing_mode

            elif k == 27:
                break

        crop1 = img2_UnDistort[:, :img_x]

        print(img_x)
        x1 = img_x
        print('첫번째사진 crop완료')


        while(1):

            cv2.imshow('image', img3_UnDistort)

            k = cv2.waitKey(1) & 0xFF

            if k == ord('m'):
                drawing_mode = not drawing_mode

            elif k == 27:
                break

        crop2 = img3_UnDistort[:, img_x:]

        print(img_x)
        x2 = img_x
        print('두번째사진 crop완료')


        # b, g, r = cv2.split(crop1)   # img파일을 b,g,r로 분리
        # crop3 = cv2.merge([r, g, b]) # b, r을 바꿔서 Merge
        #
        # b, g, r = cv2.split(crop2)   # img파일을 b,g,r로 분리
        # crop4 = cv2.merge([r, g, b]) # b, r을 바꿔서 Merge

        imgCuttingAndPasteResult = cv2.hconcat([crop1, crop2])

        # plt.imshow(imgCuttingAndPasteResult)

        # plt.show()

        cv2.imshow('crop_result', imgCuttingAndPasteResult)
        if easygui.ynbox('이 결과가 만족스러우십니까?', '제시', ('네.', '아니오. 다시할래요.')):
            break
        cv2.destroyWindow('crop_result')
    # if 1,2 or 1.5,3 합친게 마음에 안들어
        # 다시 이함수 처음부터

    cv2.destroyWindow('crop_result')

    cv2.destroyWindow('image')
    print('----------------------------')
    return imgCuttingAndPasteResult, x1, x2