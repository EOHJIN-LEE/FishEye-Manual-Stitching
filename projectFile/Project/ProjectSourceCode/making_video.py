import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('../imgs/ty_test/*.jpg'):
    img = cv2.imread(filename)
    #print(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

#print(len(img_array))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test2.avi', fourcc, 30, size)

for i in range(len(img_array)):
   out.write(img_array[i])
out.release()


# # 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class

# # vidcap = cv2.VideoCapture('../movie/test.avi')
# vidcap = cv2.VideoCapture('../imgs/video/3.MOV')
# count = 0
#
# while vidcap.isOpened():
#     ret, image = vidcap.read()
#     if 600 <= count <= 900:
#         count2 = count + 600
#         cv2.imwrite("../imgs/ty_test/3/frame%03d.jpg" % count2, image)
#         print('Saved frame%d.jpg' % count2)
#
#     count += 1
#     if count > 901:
#         break
#
# vidcap.release()

