import true
import cv2
import glob
import time


if __name__ == '__main__':
    # vidcap = cv2.VideoCapture('../movie/test.avi')
    vidcap1 = cv2.VideoCapture('../imgs/video/1.mp4')
    vidcap2 = cv2.VideoCapture('../imgs/video/2.mp4')
    vidcap3 = cv2.VideoCapture('../imgs/video/3.mp4')
    count = 0

    while vidcap1.isOpened():
        ret, image = vidcap1.read()
        if 0 <= count <= 330:
            count2 = count + 0
            cv2.imwrite("../imgs/ty_test/1/frame%03d.jpg" % count2, image)
            print('Saved frame%d.jpg' % count2)

        count += 1
        if count > 330:
            break

    vidcap1.release()

####################################

    count = 0
    while vidcap2.isOpened():
        ret, image = vidcap2.read()
        if 3 <= count <= 333:
            count2 = count - 3
            cv2.imwrite("../imgs/ty_test/2/frame%03d.jpg" % count2, image)
            print('Saved frame%d.jpg' % count2)

        count += 1
        if count > 333:
            break

    vidcap2.release()

########################################

    count = 0
    while vidcap3.isOpened():
        ret, image = vidcap3.read()
        if 12 <= count <= 342:
            count2 = count - 12
            cv2.imwrite("../imgs/ty_test/3/frame%03d.jpg" % count2, image)
            print('Saved frame%d.jpg' % count2)

        count += 1
        if count > 342:
            break

            vidcap3.release()

    # ##############################
    meFirst = True
    count = 0

    while True:
        # print('hello~~')
        if meFirst:
            start = time.time()

        img1 = cv2.imread('../imgs/ty_test/1/frame%03d.jpg' % count, -1)
        img2 = cv2.imread('../imgs/ty_test/2/frame%03d.jpg' % count, -1)
        img3 = cv2.imread('../imgs/ty_test/3/frame%03d.jpg' % count, -1)
        meFirst = False
        count += 1

        true.hello(img1, img2, img3)
        if count == 330:
            break

    timecheck = time.time() - start
    print("time :", timecheck)  # 현재시각 - 시작시간 = 실행 시간
    print("FPS : ", 330 / timecheck)


# --------------------------------------------------------


    img_array = []
    for filename in glob.glob('../imgs/ty_test/*.jpg'):
        img = cv2.imread(filename)
        # print(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    # print(len(img_array))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('test2.avi', fourcc, 30, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
