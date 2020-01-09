import numpy as np
import cv2
import math
import numpy.linalg as lin
import FourPointSelect
from tkinter import Tk
from tkinter import messagebox
import pyautogui
import easygui

root = Tk()

def matrix_verification(M): # M = homographyMatrix

    if (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0] < 0 or math.sqrt(M[0, 0] ** 2 + M[0, 1] ** 2) > 4 or math.sqrt(M[1, 0] ** 2 + M[1, 1] ** 2) < 0.1 or math.sqrt(M[1, 0] ** 2 + M[1, 1] ** 2) < 0.1 or math.sqrt(M[2, 0] ** 2 + M[2, 1] ** 2) > 0.002):
        print("문제있는 행렬입니다")
        return False
    else:
        return True


def transform_image_for(img_Source_UnDistort_Scaling, img_Destination_UnDistort_Scaling, direction, matrixCondition):
    # sift = cv2.xfeatures2d.SIFT_create()
    #
    # # find the keypoints and descriptors with SIFT
    #
    # kp1, des1 = sift.detectAndCompute(img_Source_UnDistort_Scaling, None)
    # kp2, des2 = sift.detectAndCompute(img_Destination_UnDistort_Scaling, None)
    #
    # FLANN_INDEX_KDTREE = 0
    # index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    # search_params = dict(checks=50)
    #
    # flann = cv2.FlannBasedMatcher(index_params, search_params)
    #
    # matches = flann.knnMatch(des1, des2, k=2)
    #
    # good = []
    # for m, n in matches:
    #     if m.distance < 0.7 * n.distance:
    #         good.append(m)

    # if len(good) > 0:

        # src_pts2 = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        # dst_pts3 = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    while True:
        if direction is "right":

            # homographyMatrix, mask = cv2.findHomography(src_pts2, dst_pts3, cv2.RANSAC, 5.0)  # 2 -> 3로 가는 매트릭스를 구함.
            # matchesMask = mask.ravel().tolist()
            # draw_params = dict(matchColor=(0, 255, 0),singlePointColor=None,matchesMask=matchesMask,flags=2)
            # feature_result = cv2.drawMatches(img_Source_UnDistort_Scaling, kp1, img_Destination_UnDistort_Scaling, kp2,
            #                                  good, None, **draw_params)
            #
            # feature_result_resize = cv2.resize(feature_result, dsize=(0, 0), fx=0.7, fy=1.0,
            #                                    interpolation=cv2.INTER_LINEAR)
            # cv2.imshow("dst", feature_result_resize)
            # 어떻게 매칭되는지 표시하려고

            src_pts2_new, dst_pts3_new = FourPointSelect.pickme("test12", img_Source_UnDistort_Scaling,img_Destination_UnDistort_Scaling, direction)
            print('done')
            homographyMatrix, mask = cv2.findHomography(np.float32(src_pts2_new), np.float32(dst_pts3_new), cv2.RANSAC, 5.0)  # 2 -> 3로 가는 매트릭스를 구함.

        elif direction is "left":

            # homographyMatrix, mask = cv2.findHomography(dst_pts3, src_pts2, cv2.RANSAC, 5.0)  # 2 -> 3로 가는 매트릭스를 구함.
            #
            # matchesMask = mask.ravel().tolist()
            # draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, matchesMask=matchesMask, flags=2)
            # feature_result = cv2.drawMatches(img_Source_UnDistort_Scaling, kp1, img_Destination_UnDistort_Scaling, kp2,
            #                                  good, None, **draw_params)
            # feature_result_resize = cv2.resize(feature_result, dsize=(0, 0), fx=0.7, fy=1.0, interpolation=cv2.INTER_LINEAR)
            # cv2.imshow("dst", feature_result_resize)

            dst_pts3_new, src_pts2_new = FourPointSelect.pickme("test21", img_Destination_UnDistort_Scaling, img_Source_UnDistort_Scaling, direction)
            print('done')
            homographyMatrix, mask = cv2.findHomography(np.float32(dst_pts3_new), np.float32(src_pts2_new), cv2.RANSAC, 5.0)  # 2 -> 3로 가는 매트릭스를 구함.

        else:
            print("잘못된 입력입니다.")
            return 0

        if matrixCondition is "inverse":  # 역행렬로 구하고 싶다면
            homographyMatrix = lin.inv(homographyMatrix)
        else:  # 아니라면 평범하게
            homographyMatrix = homographyMatrix
            
        # while not matrix_verification(homographyMatrix):
        #     print("하이루")
        #     break
        #     # 여기다가 태윤이의 호모그라피를 넣어주면 됌

        rows, cols = img_Destination_UnDistort_Scaling.shape[:2]

        print("호모그래프")
        print(homographyMatrix)

        result = cv2.warpPerspective(img_Destination_UnDistort_Scaling, homographyMatrix, (cols + 1000, rows))

        cv2.imshow('homo-image_result', result)

        root.withdraw()

        if easygui.ynbox('이 결과가 만족스러우십니까?', '제시', ('네.', '아니오. 다시할래요.')):
            break

    return result, homographyMatrix