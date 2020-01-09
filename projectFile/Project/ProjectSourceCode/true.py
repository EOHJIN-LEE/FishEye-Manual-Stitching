import numpy as np
from matplotlib import pyplot as plt
import cv2
import glob
import CalibrationClass
import random
import os
import ImageCuttingAndPasteClass
import argparse
import sys
import math
import TranformImageClass
import easygui

#추가수정 - 1. right하면 수정 될 왼쪽 사진 먼저 뜨고 오른쪽 나중에 뜸
#               left하면 수정 될 오른쪽 사진 먼저 뜨고 왼쪽 나중에 뜸
count = 0

isThisFirst = True  # 처음 설정시에는 트루 두번째부터는 False

homoMatrix12 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
homoMatrix32 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
img12_x = 0
img12_x2 = 0
img32_x = 0
img32_x2 = 0


# if __name__ == '__main__':
#     # 지정해서 자르기
#     # stitcher = cv2.createStitcher(False)


def hello(img1, img2, img3):
    # print('nicetomeetyou')
    global count, isThisFirst, img12_x, img32_x, img12_x2, img32_x2
    global homoMatrix12
    global homoMatrix32

    while True:
        DIM = (1280, 960)

        K = np.array([[652.8609862494474 / 2, 0.0, 1262.1021584894233 / 2], [0.0, 653.1909758659955 / 2, 928.0871455436396 / 2], [0.0, 0.0, 1.0]])
        D = np.array([[-0.024092199861108887/2], [0.002745976275100771/2], [0.002545415522352827/2], [-0.0014366825722748522/2]])

        # img1 = cv2.imread('../imgs/ty_test/1/frame000.jpg', -1)
        img1_ReSize = cv2.resize(img1, dsize=(1280, 960), interpolation=cv2.INTER_AREA)

        # img2 = cv2.imread('../imgs/ty_test/2/frame000.jpg',-1)
        img2_ReSize = cv2.resize(img2, dsize=(1280, 960), interpolation=cv2.INTER_AREA)

        # img3 = cv2.imread('../imgs/ty_test/3/frame000.jpg', -1)
        img3_ReSize = cv2.resize(img3, dsize=(1280, 960), interpolation=cv2.INTER_AREA)

        # img1_UnDistort = img1_ReSize
        # img2_UnDistort = img2_ReSize
        # img3_UnDistort = img3_ReSize

        img1_UnDistort = CalibrationClass.undistort(img1_ReSize, K, D, DIM)
        img2_UnDistort = CalibrationClass.undistort(img2_ReSize, K, D, DIM)
        img3_UnDistort = CalibrationClass.undistort(img3_ReSize, K, D, DIM)

        dst1 = img1_UnDistort.copy()
        dst2 = img2_UnDistort.copy()
        dst3 = img3_UnDistort.copy()

        Cutting_Size_Start = (40/100)
        Cutting_Size_Last = (60/100)

        # img1_UnDistort_Scaling = img1_UnDistort[int(img2_UnDistort.shape[0] * (Cutting_Size_Start)):(int)(img2_UnDistort..
        # shape[0] * (Cutting_Size_Last)), 0:img2_UnDistort.shape[1]]
        # img2_UnDistort_Scaling = img2_UnDistort[int(img2_UnDistort.shape[0] * (Cutting_Size_Start)):(int)(img2_UnDistort.shape[0] * (Cutting_Size_Last)), 0:img2_UnDistort.shape[1]]
        # img3_UnDistort_Scaling = img3_UnDistort[int(img3_UnDistort.shape[0] * (Cutting_Size_Start)):(int)(img3_UnDistort.shape[0] * (Cutting_Size_Last)), 0:img2_UnDistort.shape[1]]

        img1_UnDistort_Scaling = img1_UnDistort
        img2_UnDistort_Scaling = img2_UnDistort
        img3_UnDistort_Scaling = img3_UnDistort

        cv2.imwrite('../imgs/undistort1.jpg', img1_UnDistort_Scaling)
        cv2.imwrite('../imgs/undistort2.jpg', img2_UnDistort_Scaling)
        cv2.imwrite('../imgs/undistort3.jpg', img3_UnDistort_Scaling)

        rap = cv2.imread("../imgs/undistort1.jpg")
        foo = cv2.imread("../imgs/undistort2.jpg")
        bar = cv2.imread("../imgs/undistort3.jpg")

        # 여기까지 피는 것

        img1_UnDistort_Scaling = rap
        img2_UnDistort_Scaling = foo
        img3_UnDistort_Scaling = bar

        # cv2.imshow('1', img1_UnDistort_Scaling)
        # cv2.imshow('2', img2_UnDistort_Scaling)

        # img1_result = TranformImageClass.transform_image_for(img1_UnDistort_Scaling, img2_UnDistort_Scaling, "left", "invers", False) # left -> left 일때가 가장 괜찮음.
        # img1_result_inv = TranformImageClass.transform_image_for(img2_UnDistort_Scaling, img1_UnDistort_Scaling,"left", "inverse", False)

        if isThisFirst:  # 처음으로 설정을 하는 경우는
            # cv2.imshow('test111', img1_result)
            # cv2.imshow('testinverse', img1_result_inv)
            img1_result, homoMatrix12 = TranformImageClass.transform_image_for(img2_UnDistort_Scaling, img1_UnDistort_Scaling, "right", "inverse")

            img3_result, homoMatrix32 = TranformImageClass.transform_image_for(img2_UnDistort_Scaling, img3_UnDistort_Scaling, "left", "a")
            # img3_result_inv = TranformImageClass.transform_image_for(img2_UnDistort_Scaling, img3_UnDistort_Scaling, "left", "inverse", True)
            # print('2, 3 사진 실행 종료')

            # cv2.imshow('trasnform_result1', img1_result)
            # cv2.imshow('trasnform_result1_inv', img1_result_inv)
            # cv2.imshow('trasnform_result3', img3_result)
            # cv2.imshow('trasnform_result3_inv', img3_result_inv)

            # 비율 맞춰서 잘라주기

            cv2.destroyAllWindows()

            cv2.namedWindow('image')
            # cv2.setMouseCallback('image', ImageCuttingAndPasteClass.mouse_callback)

            ImageCuttingAndPasteResult_First_To_Second, img12_x, img12_x2 = ImageCuttingAndPasteClass.CuttingAndPaste(img1_result, img2_UnDistort_Scaling)

            # b, g, r = cv2.split(ImageCuttingAndPasteResult_First_To_Second)  # img 파일을 b,g,r로 분리
            # ImageCuttingAndPasteResult_First_To_Second = cv2.merge([r, g, b])  # b, r을 바꿔서 Merge

            cv2.namedWindow('image')

            # cv2.setMouseCallback('image', ImageCuttingAndPasteClass.mouse_callback)
            ImageCuttingAndPasteResult_Second_To_Third, img32_x, img32_x2= ImageCuttingAndPasteClass.CuttingAndPaste(ImageCuttingAndPasteResult_First_To_Second, img3_result)

            # b, g, r = cv2.split(ImageCuttingAndPasteResult_Second_To_Third)  # img 파일을 b,g,r로 분리
            # ImageCuttingAndPasteResult_Second_To_Third= cv2.merge([r, g, b])  # b, r을 바꿔서 Merge

            cv2.imshow('real_result', ImageCuttingAndPasteResult_Second_To_Third)

            if easygui.ynbox('최종결과입니다 \n이 결과가 만족스러우십니까!!! \n[네] 클릭 시 저장됩니다 \n[아니오] 클릭 시 처음부터 시작합니다', '제시', ('네.', '아니오. 다시할래요.')):
                break
        else:
            rows, cols = img3_UnDistort_Scaling.shape[:2]
            result1 = cv2.warpPerspective(img1_UnDistort_Scaling, homoMatrix12, (cols+1000, rows))
            result2 = cv2.warpPerspective(img3_UnDistort_Scaling, homoMatrix32, (cols+1000, rows))

            crop1 = result1[:, :img12_x]
            crop2 = img2_UnDistort_Scaling[:, img12_x2:]
            imgCuttingAndPasteResult12 = cv2.hconcat([crop1, crop2])

            crop1 = imgCuttingAndPasteResult12[:, :img32_x]
            crop2 = result2[:, img32_x2:]
            ImageCuttingAndPasteResult_Second_To_Third = cv2.hconcat([crop1, crop2])
            # ImageCuttingAndPasteResult_First_To_Second = ImageCuttingAndPasteClass.CuttingAndPaste(result1, img2)
            # ImageCuttingAndPasteResult_Second_To_Third = ImageCuttingAndPasteClass.CuttingAndPaste(ImageCuttingAndPasteResult_First_To_Second, result2)
            # print('yo')
            break


    isThisFirst = False
    cv2.imwrite('../imgs/ty_test/result%03d.jpg' % count, ImageCuttingAndPasteResult_Second_To_Third)
    # print('hi')
    count += 1
    cv2.destroyAllWindows()