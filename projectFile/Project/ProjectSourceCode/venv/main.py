import numpy as np
import cv2


imageA = cv2.imread('./pano_1.jpeg') # 왼쪽 사진
imageB = cv2.imread('./pano_2.jpeg') # 오른쪽 사진

grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kpA, desA = sift.detectAndCompute(grayA, None)
kpB, desB = sift.detectAndCompute(grayB, None)


bf = cv2.BFMatcher()
matches = bf.match(desA,desB)


sorted_matches = sorted(matches, key = lambda x : x.distance)
res = cv2.drawMatches(imageA, kpA, imageB, kpB, sorted_matches[:30], None, flags = 2)

cv2.imshow('res', res)