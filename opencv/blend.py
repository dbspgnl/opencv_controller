import cv2
import numpy as np
import time

def nothing(x):
    pass

def ImageBlendingOnVideo(first, second):
    print(first)
    print(second)

    video = cv2.VideoCapture(first)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    im2 = cv2.imread(second)
    im2 = cv2.resize(im2, dsize=(width, height), interpolation=cv2.INTER_AREA)
    
    cv2.namedWindow("ImageP")
    cv2.createTrackbar('Mixing', 'ImageP', 0,100 , nothing)
    mix = cv2.getTrackbarPos('Mixing','ImageP')
    
    fps = video.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)-10 #오차
    
    start_time = time.time()
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
        img = cv2.addWeighted(frame, float(100-mix)/100, im2 , float(mix)/100, 0)
        cv2.imshow("ImageP",img)
        k = cv2.waitKey(delay)
        if k == 27:
            break
        mix = cv2.getTrackbarPos("Mixing","ImageP")
        
    end_time = time.time()
    print(round(end_time-start_time,3))
    cv2.destroyAllWindows()

