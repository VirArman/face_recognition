#!/usr/bin/env python3
from facedb import FaceDB as fdb
import cv2 as cv
import os
# need to find out how get all faces or other way of comparing of input face with db faces

db = fdb(
    path="facedata",
)


def face_recognition():
    video_capture = cv.VideoCapture(0)
    counter = 0
    while True:
        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break 
        
        if counter % 10 == 0:
            recognized = db.recognize(img=video_frame, include=['name'])
        font = cv.FONT_HERSHEY_SIMPLEX
        if recognized:
            cv.putText(video_frame,recognized['name'],(10,450), font, 2,(0,255,0),2,cv.LINE_AA)
        else:
            cv.putText(video_frame,"Unknown Face",(10,450), font, 2,(0,0,255),2,cv.LINE_AA)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

        cv.imshow(
            "My Face Recognition Project", video_frame
        )
        counter += 1
    video_capture.release()
    cv.destroyAllWindows()
    return video_frame

def main():
    face_recognition()

if __name__ == "__main__":
    main()
